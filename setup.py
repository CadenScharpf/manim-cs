from setuptools import setup, find_packages


setup(
    name='manimcs',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'manim==0.17.3',
        # Add any other dependencies here
    ],
    author='Caden Scharpf',
    author_email='caden.scharpf@icloud.com',
    description='An Animation Library for Explanitory Computer Science Videos',
    long_description=open("README.MD").read(),
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