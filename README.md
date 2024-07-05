# Add SMIL path morphing to SVG files

This script adds SMIL path morphing animations to an SVG file. You need to provide the original SVG file and the target SVG file. The script will generate a new SVG file with the animations. The path nodes in the original and target SVG files must have the same number of nodes and the same node type.

## Setup

```bash
pip -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py spline examples/chicken_anim_start.svg examples/chicken_anim_target.svg --output examples/animated_chicken.svg
```
