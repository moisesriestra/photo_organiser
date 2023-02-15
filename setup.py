from setuptools import setup, find_packages

setup(
    author="Moisés Riestra González",
    author_email='moi.riestra@gmail.com',
    python_requires='>=3.6',
    description="This project aimed to be a personal tool for picture self-organization in order to avoid duplicate images.",
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