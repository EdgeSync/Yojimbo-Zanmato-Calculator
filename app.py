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

# Game version constants
VERSION_ORIGINAL = "original"  # North American & Original Japanese
VERSION_INTERNATIONAL = "international"  # International/PAL/HD Remaster

GOAL_LABELS = {
    GOAL_TRAINING: "To train as a summoner",
    GOAL_DESTROY_FIENDS: "To gain the power to destroy fiends", 
    GOAL_STRONG: "To defeat the most powerful of enemies"
}

# Version-specific settings
VERSION_SETTINGS = {
    VERSION_ORIGINAL: {
        "name": "NTSC/Original Japanese",
        "starting_compatibility": 50,
        "compatibility_divisor": 30,
        "overdrive_bonus": 2,
        "gil_multiplier": 2
    },
    VERSION_INTERNATIONAL: {
        "name": "PAL/International/HD Remaster", 
        "starting_compatibility": 128,
        "compatibility_divisor": 10,
        "overdrive_bonus": 20,
        "gil_multiplier": 4
    }
}

def get_gil_motivation(gil_offered, version):
    """Get motivation value using correct GameFAQs logarithmic formula."""
    if gil_offered <= 1:
        return 0
    
    # GameFAQs formula: ([ln(P)/ln(2)] - 1) * multiplier
    settings = VERSION_SETTINGS[version]
    motivation = (math.log(gil_offered) / math.log(2) - 1) * settings["gil_multiplier"]
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


def calculate_paid_zanmato_value(compatibility, total_gil, payment, zanmato_level, hiring_goal, overdrive, version):
    """
    Calculate the Zanmato value for a paid Zanmato attempt.
    Uses correct GameFAQs formulas for both game versions.
    """
    settings = VERSION_SETTINGS[version]
    
    # Step 1: Gil motivation from GameFAQs logarithmic formula
    motivation1 = get_gil_motivation(payment, version)
    
    # Step 2: Compatibility contribution
    compat_contribution = math.floor(compatibility / settings["compatibility_divisor"])
    motivation2 = motivation1 + compat_contribution
    
    # Step 3: Payment ratio (only applies if training goal chosen)
    if hiring_goal == GOAL_TRAINING and total_gil > 0:
        payment_ratio = payment / total_gil
        ratio_factor = 0.75 + (payment_ratio * 0.5)
        motivation3 = math.floor(motivation2 * ratio_factor)
    else:
        motivation3 = motivation2
    
    # Step 4: Zanmato level multiplier
    level_mult = get_level_multiplier(zanmato_level, hiring_goal)
    motivation4 = math.floor(motivation3 * level_mult)
    
    # Step 5: Overdrive bonus
    overdrive_bonus = settings["overdrive_bonus"] if overdrive else 0
    motivation5 = motivation4 + overdrive_bonus
    
    
    # Step 6: Random factor (0-63 will be added)
    # We return the base value before random is applied
    
    return {
        "min_value": motivation5,  # random = 0
        "max_value": motivation5 + 63,  # random = 63
        "gil_motivation": motivation1,
        "compatibility_contribution": compat_contribution,
        "ratio_applied": hiring_goal == GOAL_TRAINING,
        "level_multiplier": level_mult,
        "overdrive_bonus": overdrive_bonus,
        "motivation_steps": {
            "step1_gil": motivation1,
            "step2_compat": motivation2,
            "step3_ratio": motivation3,
            "step4_level": motivation4,
            "step5_overdrive": motivation5
        }
    }


def calculate_zanmato_probability(compatibility, total_gil, payment, zanmato_level, hiring_goal, overdrive, version):
    """
    Calculate probability of Zanmato.
    Zanmato occurs when final value >= 80
    """
    result = calculate_paid_zanmato_value(compatibility, total_gil, payment, zanmato_level, hiring_goal, overdrive, version)
    
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
        "probability": round(probability, 2),
        "guaranteed": guaranteed,
        "min_value": min_val,
        "max_value": max_val,
        "breakdown": result
    }


def find_minimum_gil(compatibility, total_gil, zanmato_level, hiring_goal, overdrive, version):
    """Binary search to find minimum gil for guaranteed Zanmato, or best achievable."""
    left, right = 0, MAX_GIL
    guaranteed_result = None
    best_result = None
    best_probability = 0
    
    # First, try to find guaranteed Zanmato
    while left <= right:
        mid = (left + right) // 2
        calc = calculate_zanmato_probability(compatibility, total_gil, mid, zanmato_level, hiring_goal, overdrive, version)
        
        if calc["guaranteed"]:
            guaranteed_result = mid
            right = mid - 1  # Try to find lower amount
        else:
            left = mid + 1
    
    # If guaranteed was found, return it
    if guaranteed_result is not None:
        return {
            "type": "guaranteed",
            "minimum_gil": guaranteed_result,
            "probability": 100.0
        }
    
    # No guaranteed found, find the best achievable percentage
    # Test key payment amounts to find the maximum probability
    test_amounts = []
    
    # Add powers of 2 up to MAX_GIL (this covers the logarithmic nature of gil motivation)
    power = 1
    while power <= MAX_GIL:
        test_amounts.append(power)
        power *= 2
    
    # Add some intermediate values for better coverage
    for base in [100, 1000, 10000, 100000, 1000000]:
        for mult in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            amount = base * mult
            if amount <= MAX_GIL:
                test_amounts.append(amount)
    
    # Test all amounts and find the best
    for amount in sorted(set(test_amounts)):
        calc = calculate_zanmato_probability(compatibility, total_gil, amount, zanmato_level, hiring_goal, overdrive, version)
        if calc["probability"] > best_probability:
            best_probability = calc["probability"]
            best_result = amount
    
    return {
        "type": "best_effort",
        "minimum_gil": best_result,
        "probability": best_probability
    }


@app.route('/')
def index():
    """Main page with calculator interface."""
    enemy_list = get_enemy_names()
    return render_template('index.html', 
                          enemies=enemy_list,
                          goal_labels=GOAL_LABELS,
                          version_settings=VERSION_SETTINGS,
                          default_version=VERSION_INTERNATIONAL)


@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate Zanmato probability or minimum gil."""
    try:
        data = request.json
        
        # Get version (default to International for HD Remaster)
        version = data.get('version', VERSION_INTERNATIONAL)
        if version not in VERSION_SETTINGS:
            version = VERSION_INTERNATIONAL
        
        enemy_name = data.get('enemy')
        compatibility = int(data.get('compatibility', VERSION_SETTINGS[version]["starting_compatibility"]))
        if compatibility < 0 or compatibility > 255:
            return jsonify({"error": "Compatibility must be between 0 and 255."}), 400
        total_gil = int(data.get('total_gil', 0))
        if total_gil < 0:
            return jsonify({"error": "Total gil owned cannot be negative."}), 400
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
            result_data = find_minimum_gil(compatibility, total_gil, zanmato_level, hiring_goal, overdrive, version)
            
            if result_data is None:
                return jsonify({"error": "Cannot calculate Zanmato probabilities with these parameters"}), 400
            
            min_gil = result_data["minimum_gil"]
            
            # Calculate detailed breakdown at that payment
            detailed_result = calculate_zanmato_probability(compatibility, total_gil, min_gil, zanmato_level, hiring_goal, overdrive, version)
            
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
                "version": version,
                "version_name": VERSION_SETTINGS[version]["name"]
            })
        else:  # probability calculation
            payment = int(data.get('payment', 0))
            
            # Validate payment amount - Yojimbo dismisses if offered 0 gil
            if payment <= 0:
                return jsonify({"error": "Gil payment must be greater than 0. Yojimbo dismisses if offered 0 gil."}), 400
            
            result = calculate_zanmato_probability(compatibility, total_gil, payment, zanmato_level, hiring_goal, overdrive, version)
            
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
                "version": version,
                "version_name": VERSION_SETTINGS[version]["name"]
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


@app.route('/images/<filename>')
def serve_image(filename):
    """Serve enemy images from the images directory."""
    return send_from_directory('images', filename)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
