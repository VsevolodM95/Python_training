try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Pro',
    'author': 'Vsevolod Metelsky',
    'url': '...',
    'download_url': '...',
    'author_email': 'lordmilten95@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Game'],
    'scripts': [],
    'name': 'Game'
}

setup(**config)
