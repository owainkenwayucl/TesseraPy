# TesseraPy

TesseraPy provides a minimal wrapper for HP/Google's Tesseract OCR library, making use of CFFI instead of running the `tesseract` executable like other Python wrappers.

Currently (v0.1.4), it is extremely minimal having a class called `tesseract` with a single method `get_text()` which takes a PIL image as an argument and returns the text in the image.

So e.g.

```python
import TesseraPy
from PIL import Image

i = Image.open("test.png")
t = TesseraPy.tesseract()
txt = t.get_text(i)
print(txt)
```

## Installation

```
pip install git+https://github.com/owainkenwayucl/TesseraPy
```

To install a specific version, e.g. the first release, v0.1.4

```
pip install git+https://github.com/owainkenwayucl/TesseraPy.git@v0.1.4
```

