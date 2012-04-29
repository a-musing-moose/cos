#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Run: python setup.py sdist upload
"""

from setuptools import setup, find_packages

setup(name='cos',
      version='0.0.1',
      url='https://github.com/a-musing-moose/cos',
      author="Jonathan Moss",
      author_email="jonathan.moss@tangentone.com.au",
      description="A cloud scalable object store with a ZeroMQ interface",
      long_description=open('README.rst').read(),
      keywords="ZeroMQ, Scalable, Cloud, Services",
      license='BSD',
      platforms=['linux'],
      packages=find_packages(exclude=["*.tests"]),
      include_package_data = True,
      install_requires=[
          'pyzmq==2.1.11',
          'pymongo==2.1.1',
          'python-daemon==1.6',
          ],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Environment :: No Input/Output (Daemon)',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python']
      )
