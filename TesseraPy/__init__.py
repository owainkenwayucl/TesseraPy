from PIL import Image
from cffi import FFI
import os

TESSERACT_CDEFS = """
typedef struct TessBaseAPI TessBaseAPI;

TessBaseAPI* TessBaseAPICreate(void);

int TessBaseAPIInit3(TessBaseAPI* handle,
                     const char* datapath,
                     const char* language);

void TessBaseAPISetImage(TessBaseAPI* handle, 
                         const unsigned char* imagedata,
                         int width, 
                         int height, 
                         int bytes_per_pixel, 
                         int bytes_per_line);
int TessBaseAPIRecognize(TessBaseAPI* handle, void* monitor);

char* TessBaseAPIGetUTF8Text(TessBaseAPI* handle);

void TessDeleteText(char* text);
void TessBaseAPIEnd(TessBaseAPI* handle);
void TessBaseAPIDelete(TessBaseAPI* handle);
"""

TESSERACT_ENCODING = os.environ.get("TESSERACT_ENCODING", "utf-8")
TESSERACT_LIBRARY = os.environ.get("TESSERACT_LIBRARY", "/lib64/libtesseract.so.5.3.4")
TESSERACT_DATA = os.environ.get("TESSERACT_DATA", "/usr/share/tesseract/tessdata/").encode(TESSERACT_ENCODING)
TESSERACT_LANGUAGE = os.environ.get("TESSERACT_LANGUAGE", "eng").encode(TESSERACT_ENCODING)

class tesseract:
	def __init__(self):
		self.ffi = FFI()
		self.ffi.cdef(TESSERACT_CDEFS)
		self.lib = self.ffi.dlopen(TESSERACT_LIBRARY)
		self.api = self.lib.TessBaseAPICreate()

		_ = self.lib.TessBaseAPIInit3(self.api, TESSERACT_DATA, TESSERACT_LANGUAGE)

	def get_text(self, image):
		if not isinstance(image, Image.Image):
			raise TypeError("Image is not a PIL image.")
		image = image.convert("RGB")
		width, height = image.size
		_ = self.lib.TessBaseAPISetImage(self.api, image.tobytes(), width, height, 3, 3*width)
		_ = self.lib.TessBaseAPIRecognize(self.api, self.ffi.NULL)
		text_ptr = self.lib.TessBaseAPIGetUTF8Text(self.api)
		text = ffi.string(text_ptr).decode(TESSERACT_ENCODING)

		self.lib.TessDeleteText(text_ptr)

		return text

	def __del__(self):
		self.lib.TessBaseAPIEnd(self.api)
		self.lib.TessBaseAPIDelete(self.api)
