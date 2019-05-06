import setuptools
from distutils.core import setup

setup(
  name = 'keycdn',
  packages = ['keycdn'],
  version = '0.4',
  description = 'A Python REST Client for KeyCDN API',
  long_description = open('README.md').read(),
  long_description_content_type = 'text/markdown',
  author = 'KeyCDN',
  author_email = 'hello@keycdn.com',
  url = 'https://github.com/keycdn/python-keycdn-api',
  download_url = 'https://github.com/keycdn/python-keycdn-api/tarball/0.3',
  keywords = ['cdn', 'content delivery network', 'keycdn'],
  classifiers = [],
)
