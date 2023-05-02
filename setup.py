from setuptools import setup, find_packages

setup(
    name='manimcs',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'manim==0.17.3',
        # Add any other dependencies here
    ],
)
