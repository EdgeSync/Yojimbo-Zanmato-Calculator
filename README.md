# Yojimbo Zanmato Calculator

A web-based calculator for Final Fantasy X that estimates the probability of Yojimbo performing his **Zanmato** one-hit-kill attack, based on the formulas documented in the Dansg08 YouTube Video.

Supports **PAL/International/HD Remaster** versions of the game.

## Try it Out

There is a version hosted here: https://yojimbocalc.pythonanywhere.com/
Hop on over and try it out. 

## Features

- Calculate Zanmato probability for a given gil payment
- Find the minimum gil required for the best possible chance
- Enemy database with Zanmato levels, stats, and images
- Compatibility change reference table
- Dual version support (NTSC vs PAL/International/Remaster)

## Setup

**1. Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**2. Install dependencies:**
```bash
pip3 install flask
```

**3. Run the app:**
```bash
python3 app.py
```

**4. Open your browser and go to:**
```
http://127.0.0.1:5000
```

## Resources

- [Final Fantasy X – Yojimbo FAQ](https://gamefaqs.gamespot.com/ps2/197344-final-fantasy-x/faqs/24392) by jobber2022497
- [Yojimbo Zanmato Deep Dive](https://www.youtube.com/watch?v=Gix4qXFzlxg) by Dansg08
- [Steam Guide - Yojimbo Calculator](https://steamcommunity.com/sharedfiles/filedetails/?l=german&id=699497723) by rodrigo_vda
- [FFX Wiki - Enemies](https://finalfantasy.fandom.com/wiki/Final_Fantasy_X_enemies)
