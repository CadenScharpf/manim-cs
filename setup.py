import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='manimcs',
    version='0.4.3',
    packages=find_packages(),
    install_requires=[
        'manim==0.17.3',
        # Add any other dependencies here
    ],
    author='Caden Scharpf',
    author_email='caden.scharpf@icloud.com',
    description='An Animation Library for Explanitory Computer Science Videos',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CadenScharpf/manim-cs',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
