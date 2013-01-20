try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
        'description': 'My flashcard program for study',
        'author': 'Adames',
        'download_url': 'https://github.com/Adames/flashcardHARD',
        'author_email': 'adames.hodelin@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['flashcardHARD'],
        'scripts': [],
        'name': 'flashcardHARD'
}

setup(**config)
