try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Pizza-bot',
    'author': 'Ruslan Afanasiev, Viktor Berlov',
    'url': 'http://pizza-bot.kiev.ua',
    'download_url': 'https://github.com/rafanasiev/pizza-bot',
    'author_email': 'info@pizza-bot.kiev.ua',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Pizza-bot'],
    'scripts': [],
    'name': 'pizza-bot'
}

setup(**config)
