#!/usr/bin/env python
from setuptools import setup
f = open('README.md','r')
long_description = f.read()
setup(name = 'reporter_su',
      version = '0.1.1',
      description = 'check your task and when it finished, you will receive a email',
      long_description = long_description,
      long_description_content_type="text/markdown",
      author = 'Su Jiaqi',
      author_email = 'luskyqi@outlook.com',
      python_requires = ">=3.0",
      url = 'https://github.com/ZeroDesigner/reporter_su.git',
      packages = ['reporter_su'],
      license = 'MIT',
      keywords = ['python', 'email', 'pbs']
      )
