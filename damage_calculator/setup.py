# setup.py

from setuptools import setup, find_packages

setup(
    name="damage_calculator",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'damage_calculator = damage_calculator.calculator:main',
        ],
    },
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Pokemon damage calculator",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/siro-rai/pokemon_damade_ver.2.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
