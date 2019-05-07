import setuptools
from distutils.core import setup

setup(
  name = 'keycdn',
  packages = ['keycdn'],
  version = '0.4.3',
  description = 'A Python REST Client for KeyCDN API',
  long_description = open('README.md').read(),
  long_description_content_type = 'text/markdown',
  author = 'KeyCDN',
  url = 'https://github.com/keycdn/python-keycdn-api',
  keywords = ['cdn', 'content delivery network', 'keycdn'],
  classifiers = [
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3'
  ],
  install_requires=[
    'requests>=2.11.1',
  ],
)
