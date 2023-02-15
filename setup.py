from setuptools import setup, find_packages

setup(
    name='photo_organiser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'photo_organiser = photo_organiser.cli:main',
        ],
    },
)