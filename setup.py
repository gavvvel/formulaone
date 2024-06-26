# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='formulaone',
    version='0.1.0',
    description='Downloads and prepares formula one data',
    long_description=readme,
    author='Fernando Azevedo',
    author_email='fernandoazevedo165@gmail.com',
    url='https://github.com/gavvvel/formulaone',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
