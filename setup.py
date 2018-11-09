#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='customaccount',
      version='0.1',
      packages=find_packages(),
      package_data={
          'customaccount': ['templates/*.html', 'templates/**/*.html']
      },
      include_package_data=True,
      )