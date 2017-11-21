#!/usr/bin/python
from distutils.sysconfig import get_python_lib
from setuptools import setup
from os.path import isfile, join
import glob
import os

if isfile("MANIFEST"):
	os.unlink("MANIFEST")

# Get PYTHONLIB with no prefix so --prefix installs work.
PYTHONLIB = join(get_python_lib(standard_lib=1, prefix=''), 'site-packages')

setup(name="python-linux-procfs",
      version = "0.5",
      description = "Linux /proc abstraction classes",
      author = "Arnaldo Carvalho de Melo",
      author_email = "acme@redhat.com",
      url = "http://userweb.kernel.org/python-linux-procfs",
      license = "GPLv2",
      long_description =
"""\
Abstractions to extract information from the Linux kernel /proc files.
""",
      packages = ["procfs"],
      scripts = ['pflags'],
      install_requires = ['six'],
      )
