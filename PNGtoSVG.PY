import os
import base64

startSvgTag = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1"  xmlns="http://www.w3.org/2000/svg"  xmlns:xlink="http://www.w3.org/1999/xlink"  width="800px" height="300px" viewBox="0 0 800 300">"""

endSvgTag = "</svg>"

for files in os.listdir("."):
    if files.endswith(".png"):#input direction
        pngFile = open(files, 'rb')
        base64data = base64.b64encode(pngFile.read()).replace(b'\\n', b'')
        base64String = '<image xlink:href="data:image/png;base64, {0}" width="100%" height="100%" x="0" y="0" />'.format(base64data.decode('utf-8'))
        f = open(os.path.splitext(files)[0] + ".svg", 'w')
        f.write(startSvgTag + base64String + endSvgTag)
        print('Convert ', files, 'to', os.path.splitext(files)[0], '.svg', 'Done.')
