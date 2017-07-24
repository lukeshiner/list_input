#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='list_input',
    version='0.0.1',
    description='Django Form Field for lists',
    author='Luke Shiner',
    author_email='luke@lukeshiner.com',
    packages=find_packages(),
    include_package_data=True,
    data_files=[('list_input', [
        'list_input/static/list_input/scripts/list_widget.js',
        'list_input/templates/list_input/list_widget.html'])]
    )
