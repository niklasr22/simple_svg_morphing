# Add SMIL path morphing to SVG files

This script adds SMIL path morphing animations to an SVG file. You need to provide the original SVG file and the target SVG file. The script will generate a new SVG file with the animations. The path nodes in the original and target SVG files must have the same number of nodes and the same node type.

**DISCLAIMER**: This tool is not perfect and may not work with all SVG files. It is just a quick and dirty solution to add path morphing animations to SVG files and was made for my personal use. Maybe it is useful for you too.

## Setup

```bash
pip -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Help

```bash
python main.py --help
```

## Example Usage

```bash
python main.py spline examples/chicken_anim_start.svg examples/chicken_anim_target.svg --output examples/animated_chicken.svg --repeat-count indefinite --duration 2s
```

<table>
  <tr>
    <th>Start</th>
    <th>Target</th>
    <th>Result</th>
  </tr>
  <tr>
    <td><img src="https://github.com/niklasr22/simple_svg_morphing/blob/main/examples/chicken_anim_start.svg" alt="Start SVG"/></td>
    <td><img src="https://github.com/niklasr22/simple_svg_morphing/blob/main/examples/chicken_anim_target.svg" alt="Target SVG"/></td>
    <td><img src="https://github.com/niklasr22/simple_svg_morphing/blob/main/examples/animated_chicken.svg" alt="Animated SVG"/></td>
  </tr>
</table>
