# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Flow_extraction_tests',
    version='0.1.0',
    description='Package that tests different flow extraction algorithms',
    long_description=readme,
    author='Simon van Staalduine',
    author_email='svstaalduine@amolf.nl',
    url='https://github.com/Staalduine/flow_extraction_tests',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

