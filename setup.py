#!/usr/bin/env python3

from distutils.core import setup

setup(name="TesseraPy".
      version="0.1",
      description="Minimal Python CFFI bindings for Tesseract", 
      author="Dr Owain Kenway",
      author_email="o.kenway@ucl.ac.uk",
      url="https://github.com/owainkenwayucl/TesseraPy",
      packages=["TesseraPy"],
      install_requires=["Pillow"])
