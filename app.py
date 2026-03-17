"""
Yojimbo Zanmato Calculator
Flask application for calculating Zanmato probabilities
Based on GameFAQs guide formulas - supports both game versions
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from enemies import ENEMIES, get_enemy_names, get_enemy_zanmato_level, get_enemy_info
import math
import os

app = Flask(__name__)

# Constants from the GameFAQs guide
MAX_GIL = 999999999
GOAL_TRAINING = "training"
GOAL_DESTROY_FIENDS = "destroy_fiends"
GOAL_STRONG = "strong_enemies"

# Game version for PAL/International/HD Remaster only
VERSION_INTERNATIONAL = "international"

GOAL_LABELS = {
    GOAL_TRAINING: "To train as a summoner",
    GOAL_DESTROY_FIENDS: "To gain the power to destroy fiends", 
    GOAL_STRONG: "To defeat the most powerful of enemies"
}

# Spending charts based on game analysis
SPENDING_CHARTS = {
    "levels_1_3": {
        "title": "Spending Chart - Zanmato Levels 1-3",
        "subtitle": "Percentages for Option 3 (Defeat strongest enemies) with Full Overdrive",
        "payment_ranges": ["1", "4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", 
                          "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576"],
        "compatibility_values": [0, 32, 64, 96, 128, 160, 192, 224, 255],
        "data": [
            [6, 9, 12, 17, 20, 25, 29, 32, 37],
            [10, 14, 18, 21, 25, 31, 34, 37, 42],
            [15, 18, 23, 26, 31, 35, 39, 43, 46],
            [20, 25, 28, 31, 35, 40, 43, 48, 51],
            [25, 29, 32, 37, 40, 45, 50, 53, 56],
            [31, 34, 37, 42, 45, 50, 54, 57, 62],
            [35, 39, 43, 46, 50, 56, 59, 62, 67],
            [40, 43, 48, 51, 56, 60, 64, 68, 71],
            [45, 50, 53, 56, 60, 65, 68, 73, 76],
            [50, 54, 57, 62, 65, 70, 75, 78, 81],
            [56, 59, 62, 67, 70, 75, 79, 82, 87],
            [60, 64, 68, 71, 75, 81, 84, 87, 92],
            [65, 68, 73, 76, 81, 85, 89, 94, 96],
            [70, 75, 78, 81, 85, 90, 93, 98, 100],
            [75, 79, 82, 87, 90, 95, 98, 100, 100],
            [81, 84, 87, 92, 95, 100, 100, 100, 100],
            [85, 89, 93, 96, 100, 100, 100, 100, 100],
            [90, 93, 98, 100, 100, 100, 100, 100, 100],
            [95, 100, 100, 100, 100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100, 100, 100, 100, 100]
        ]
    },
    "levels_4_6": {
        "title": "Spending Chart - Zanmato Levels 4-6",
        "subtitle": "Percentages for Option 3 (Defeat strongest enemies) with Full Overdrive",
        "payment_ranges": ["1", "4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", 
                          "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576"],
        "compatibility_values": [0, 32, 64, 96, 128, 160, 192, 224, 255],
        "data": [
            [6, 8, 9, 10, 12, 15, 17, 18, 21],
            [8, 9, 12, 14, 15, 18, 20, 21, 23],
            [11, 12, 14, 15, 18, 20, 21, 25, 26],
            [13, 15, 17, 18, 20, 23, 25, 26, 28],
            [16, 17, 18, 21, 23, 25, 28, 29, 31],
            [19, 20, 21, 23, 25, 28, 29, 31, 34],
            [20, 21, 25, 26, 28, 31, 32, 34, 36],
            [23, 25, 26, 28, 31, 32, 34, 37, 39],
            [25, 28, 29, 31, 32, 35, 37, 39, 40],
            [28, 29, 31, 34, 35, 37, 40, 42, 43],
            [31, 32, 34, 35, 37, 40, 42, 43, 46],
            [33, 34, 37, 39, 40, 43, 45, 46, 48],
            [36, 37, 39, 40, 43, 45, 46, 50, 51],
            [38, 40, 42, 43, 45, 48, 50, 51, 53],
            [41, 42, 44, 46, 48, 50, 53, 54, 56],
            [44, 45, 46, 48, 50, 53, 54, 56, 59],
            [45, 46, 50, 51, 53, 56, 57, 59, 60],
            [48, 50, 51, 53, 56, 57, 59, 62, 64],
            [50, 53, 54, 56, 57, 60, 62, 64, 65],
            [53, 54, 56, 59, 60, 62, 65, 67, 68]
        ]
    }
}

# International version settings only
VERSION_SETTINGS = {
    "name": "PAL/International/HD Remaster", 
    "starting_compatibility": 128,
    "compatibility_divisor": 10,
    "overdrive_bonus": 20,
    "gil_multiplier": 4
}

def get_gil_motivation(gil_offered):
    """Get motivation value using correct GameFAQs logarithmic formula."""
    if gil_offered <= 1:
        return 0
    
    # GameFAQs formula: ([ln(P)/ln(2)] - 1) * multiplier (International version)
    motivation = (math.log(gil_offered) / math.log(2) - 1) * VERSION_SETTINGS["gil_multiplier"]
    return math.floor(motivation)


def get_level_multiplier(zanmato_level, hiring_goal):
    """Get level multiplier based on Zanmato level and hiring answer."""
    if hiring_goal == GOAL_TRAINING or hiring_goal == GOAL_DESTROY_FIENDS:
        # First or second answer: training/destroy fiends
        multipliers = {1: 1.0, 2: 0.5, 3: 0.33, 4: 0.25, 5: 0.2}
        return multipliers.get(zanmato_level, 0.2)
    else:  # GOAL_STRONG
        # Third answer: defeat strongest enemies
        if zanmato_level <= 3:
            return 0.8
        else:  # 4-5
            return 0.4


def calculate_paid_zanmato_value(compatibility, payment, zanmato_level, hiring_goal, overdrive):
    """
    Calculate the Zanmato value for a paid Zanmato attempt.
    Uses correct formulas based on game code analysis.
    """
    
    # Step 1: Gil motivation from logarithmic formula
    gil_motivation = get_gil_motivation(payment)
    
    # Step 2: Compatibility motivation = Gil motivation + (compatibility/10)
    compatibility_motivation = gil_motivation + math.floor(compatibility / VERSION_SETTINGS["compatibility_divisor"])
    
    # Step 3: Zanmato level motivation = Compatibility motivation × choice multiplier
    level_mult = get_level_multiplier(zanmato_level, hiring_goal)
    zanmato_level_motivation = math.floor(compatibility_motivation * level_mult)
    
    # Step 4: Overdrive motivation = Zanmato level motivation + overdrive bonus
    overdrive_bonus = VERSION_SETTINGS["overdrive_bonus"] if overdrive else 0
    overdrive_motivation = zanmato_level_motivation + overdrive_bonus
    
    
    # Step 5: Random factor (0-63 will be added)
    # We return the base value before random is applied
    
    return {
        "min_value": overdrive_motivation,  # random = 0
        "max_value": overdrive_motivation + 63,  # random = 63
        "gil_motivation": gil_motivation,
        "compatibility_contribution": math.floor(compatibility / VERSION_SETTINGS["compatibility_divisor"]),
        "ratio_applied": False,  # No longer used
        "level_multiplier": level_mult,
        "overdrive_bonus": overdrive_bonus,
        "motivation_steps": {
            "step1_gil": gil_motivation,
            "step2_compatibility": compatibility_motivation,
            "step3_zanmato_level": zanmato_level_motivation,
            "step4_overdrive": overdrive_motivation
        }
    }


def calculate_zanmato_probability(compatibility, payment, zanmato_level, hiring_goal, overdrive):
    """
    Calculate probability of Zanmato.
    Zanmato occurs when final value >= 80
    """
    result = calculate_paid_zanmato_value(compatibility, payment, zanmato_level, hiring_goal, overdrive)
    
    min_val = result["min_value"]
    max_val = result["max_value"]
    
    # Guaranteed if min >= 80
    if min_val >= 80:
        probability = 100.0
        guaranteed = True
    # Impossible if max < 80
    elif max_val < 80:
        probability = 0.0
        guaranteed = False
    else:
        # Partial probability: (max - 79) / 64
        successful_randoms = max_val - 79
        probability = (successful_randoms / 64) * 100
        guaranteed = False
    
    return {
        "probability": math.floor(probability),  # Game truncates down to integer
        "guaranteed": guaranteed,
        "min_value": min_val,
        "max_value": max_val,
        "breakdown": result
    }


def find_minimum_gil(compatibility, zanmato_level, hiring_goal, overdrive):
    """Find the most efficient gil bracket for the highest achievable percentage."""
    
    # Define gil brackets based on the reference tables (powers of 2 pattern)
    gil_brackets = [1, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 
                   16384, 32768, 65536, 131072, 262144, 524288, 1048576]
    
    # Test each bracket (using minimum amount in bracket for efficiency)
    best_gil = 1
    best_percentage = 0
    guaranteed_gil = None
    
    for gil_amount in gil_brackets:
        if gil_amount > MAX_GIL:
            break
            
        calc = calculate_zanmato_probability(compatibility, gil_amount, zanmato_level, hiring_goal, overdrive)
        
        # Check for guaranteed first
        if calc["guaranteed"]:
            guaranteed_gil = gil_amount
            break
            
        # Track the best non-guaranteed option
        if calc["probability"] > best_percentage:
            best_percentage = calc["probability"]
            best_gil = gil_amount
    
    # Return guaranteed if found
    if guaranteed_gil is not None:
        return {
            "type": "guaranteed",
            "minimum_gil": guaranteed_gil,
            "probability": 100
        }
    
    # Return best achievable bracket
    return {
        "type": "best_bracket",
        "minimum_gil": best_gil,
        "probability": best_percentage
    }


@app.route('/')
def index():
    """Main page with calculator interface."""
    enemy_list = get_enemy_names()
    return render_template('index.html', 
                          enemies=enemy_list,
                          goal_labels=GOAL_LABELS)


@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate Zanmato probability or minimum gil."""
    try:
        data = request.json
        
        enemy_name = data.get('enemy')
        compatibility = int(data.get('compatibility', VERSION_SETTINGS["starting_compatibility"]))
        if compatibility < 0 or compatibility > 255:
            return jsonify({"error": "Compatibility must be between 0 and 255."}), 400
        hiring_goal = data.get('hiring_goal', GOAL_TRAINING)
        if hiring_goal not in GOAL_LABELS:
            hiring_goal = GOAL_TRAINING
        overdrive = data.get('overdrive', False)
        calc_type = data.get('calc_type', 'probability')  # 'probability' or 'minimum'
        
        # Get enemy Zanmato level
        zanmato_level = get_enemy_zanmato_level(enemy_name)
        enemy_info = get_enemy_info(enemy_name)
        
        if zanmato_level is None:
            return jsonify({"error": f"Enemy '{enemy_name}' not found or cannot be Zanmato'd"}), 400
        
        if calc_type == 'minimum':
            # Find minimum gil for best Zanmato chance
            result_data = find_minimum_gil(compatibility, zanmato_level, hiring_goal, overdrive)
            
            if result_data is None:
                return jsonify({"error": "Cannot calculate Zanmato probabilities with these parameters"}), 400
            
            min_gil = result_data["minimum_gil"]
            
            # Calculate detailed breakdown at that payment
            detailed_result = calculate_zanmato_probability(compatibility, min_gil, zanmato_level, hiring_goal, overdrive)
            
            return jsonify({
                "type": "minimum_gil",
                "minimum_gil": min_gil,
                "probability": result_data["probability"],
                "guaranteed": result_data["type"] == "guaranteed",
                "result_type": result_data["type"],  # 'guaranteed' or 'best_effort'
                "breakdown": detailed_result["breakdown"],
                "enemy": enemy_name,
                "enemy_info": enemy_info,
                "zanmato_level": zanmato_level,
                "compatibility": compatibility
            })
        else:  # probability calculation
            payment = int(data.get('payment', 0))
            
            # Validate payment amount - Yojimbo dismisses if offered 0 gil
            if payment <= 0:
                return jsonify({"error": "Gil payment must be greater than 0. Yojimbo dismisses if offered 0 gil."}), 400
            
            result = calculate_zanmato_probability(compatibility, payment, zanmato_level, hiring_goal, overdrive)
            
            return jsonify({
                "type": "probability",
                "payment": payment,
                "probability": result["probability"],
                "guaranteed": result["guaranteed"],
                "min_value": result["min_value"],
                "max_value": result["max_value"],
                "breakdown": result["breakdown"],
                "enemy": enemy_name,
                "enemy_info": enemy_info,
                "zanmato_level": zanmato_level,
                "compatibility": compatibility
            })
            
    except ValueError as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/enemy/<enemy_name>')
def enemy_details(enemy_name):
    """Get detailed information about an enemy."""
    info = get_enemy_info(enemy_name)
    
    if info is None:
        return jsonify({"error": "Enemy not found"}), 404
    
    return jsonify({
        "name": enemy_name,
        "info": info
    })


@app.route('/spending-chart/<int:zanmato_level>')
def get_spending_chart(zanmato_level):
    """Get the appropriate spending chart for the given zanmato level."""
    try:
        if zanmato_level <= 3:
            chart_key = "levels_1_3"
        elif zanmato_level <= 6:
            chart_key = "levels_4_6"
        else:
            return jsonify({"error": "Invalid zanmato level"}), 400
        
        chart_data = SPENDING_CHARTS[chart_key]
        return jsonify({
            "success": True,
            "chart": chart_data
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/images/<filename>')
def serve_image(filename):
    """Serve enemy images from the images directory."""
    return send_from_directory('images', filename)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
