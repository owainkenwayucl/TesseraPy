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

## Configuration

You can control where TesseraPy looks for the various parts of Tesseract with the following environment variable:

* `TESSERACT_LIBRARY` - path to the Tesseract library - default: `/lib64/libtesseract.so.5.3.4`
* `TESSERACT_DATA` - path to Tesseract data files - default: `/usr/share/tesseract/tessdata/`
* `TESSERACT_ENCODING` - encoding - default: `utf-8`
* `TESSERACT_LANGUAGE` - language - default: `eng`

The defaults are those of the development platform - AlmaLinux 10.
