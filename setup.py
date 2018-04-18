from distutils.core import setup
from distutils.extension import Extension

extensions = [Extension("_weakref", ["_weakref.c"], language="c")]

setup(name = "_weakref", ext_modules = extensions)