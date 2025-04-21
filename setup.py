from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from Cython.Build import cythonize
from glob import glob
import numpy

# Define all C++ and Cython source files
sourcefiles = ['pyflow.pyx']
sourcefiles.extend(glob("src/*.cpp"))

extensions = [
    Extension(
        "pyflow",
        sources=sourcefiles,
        include_dirs=[numpy.get_include(), 'src'],
        language="c++",
        extra_compile_args=["-std=c++11"]
    )
]

setup(
    name="pyflow",
    version="1.0",
    description="Python wrapper for the Coarse2Fine Optical Flow code.",
    author="Deepak Pathak",
    ext_modules=cythonize(extensions),
    zip_safe=False,
    install_requires=["numpy", "cython"],
)
