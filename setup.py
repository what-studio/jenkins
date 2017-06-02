# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='jenkins-cffi',
    version='1.0.2',
    description="Python CFFI wrapper around Bob Jenkins' hash functions.",
    author='What! Studio',
    maintainer='Heungsub Lee',
    maintainer_email='sub@subl.ee',
    url='https://github.com/what-studio/jenkins-cffi/',
    packages=['jenkins_cffi'],
    install_requires=['cffi>=1.10.0'],
    setup_requires=['cffi>=1.10.0'],
    cffi_modules=['jenkins_cffi/build.py:ffibuilder'],
)
