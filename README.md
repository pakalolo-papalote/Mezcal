[![Mezcal Bottle](https://github.org/repo-dir/mezcal.bz2.png)](https://github.org/repodir)

# Description:
Mezcal is a distilled from the awesome Agave color scheme generator application (http://home.gna.org/colorscheme/).

Depends on:
	- numpy >= 1.12.1

# Usage Example:
```python
from Mezcal.Barrel import Bottle

glass = Bottle()

# Set rgb, hsv, hex on Bottle objects.
glass.rgb = ( 100, 200, 55 )


# Get the corresponding color schemes.
print( "RGB color scheme:")
print( glass.rgb_scheme )

print( "HSV color scheme")
print( glass.hsv_scheme )

print( "Hex color scheme")
print( glass.hex_scheme )

glass.hsv = ( 360, 100, 50 )
print( glass.analogous[0].hex )

# Define hex, rgb, hsv on class creation.
glass = Bottle( hex="#0066cc" )
print( glass.rgb_scheme )
```
[![Mezcal Widget](https://github.org/repo-dir/PyQt5-widget/g.gif)](https://github.org/repodir/PyQt5-widget)

# Mezcal PyQt5 Visualization
```bash
#!/bin/bash

# Requires PyQt5 to be installed.
python widget/SampleWidget.py
```
