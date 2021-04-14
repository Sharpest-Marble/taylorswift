#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import os
import sys
from setuptools import setup

sys.path.insert(0, "taylorswiftGUI")


long_description = \
    """
taylorswiftGUI is a gui for the taylorswift library, 
which helps you find the perfect taylor swift song.

"""


setup(name='taylorswiftGUI',
      version=0.1,
      description='GUI for the famed taylorswift() function',
      packages=['taylorswiftGUI'],
      install_requires=['numpy' 'tkinter' 'taylorswift'],
      author='elliot',
      author_email='b.elliotsmith42@gmail.com',
      license='MIT',
      long_description = long_description,
      url='https://github.com/Sharpest-Marble/taylorswift',
      package_data={'': ['README.md', 'LICENSE']},
      include_package_data=True,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        ],
      )
