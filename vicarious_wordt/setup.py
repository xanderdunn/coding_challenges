"""Module information for aalgopy."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'Vicarious Problem',
    'author': 'Xander Dunn',
    'url': '',
    'download_url': '',
    'author_email': 'xander.dunn@icloud.com',
    'version': '0',
    'install_requires': ['pytest', 'nltk'],
    'packages': ['wordt'],
    'scripts': [],
    'name': 'wordt'
}

setup(**config)
