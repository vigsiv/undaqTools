# Copyright (c) 2012, Roger Lew [see LICENSE.txt]
# This software is funded in part by NIH Grant P20 RR016454.

##from distutils.core import setup
from setuptools import setup

setup(name='undaqTools',
    version='0.2.0',
    description='undaqTools is a pythonic interface to the National Advanced '\
                'Driving Simulator (NADS) Data AcQuisition (DAQ) files',
    author='Roger Lew',
    author_email='rogerlew@gmail.com',
    license = "BSD",
    classifiers=["DDevelopment Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Information Technology",
                 "Intended Audience :: Science/Research",
                 "License :: OSI Approved :: BSD License",
                 "Natural Language :: English",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: Scientific/Engineering :: Information Analysis",
                 "Topic :: Scientific/Engineering :: Mathematics",
                 "Topic :: Software Development :: Libraries :: Python Modules"],
    url='https://github.com/rogerlew/undaqTools',
    packages=['undaqTools',
              'undaqTools.deprecated',
              'undaqTools.examples',
              'undaqTools.misc',
              'undaqTools.scripts',
              'undaqTools.tests'],
    scripts=['scripts/undaq'],
    zip_safe=False)

"""C:\Python27\python.exe setup.py sdist upload --identity="Roger Lew" --sign"""