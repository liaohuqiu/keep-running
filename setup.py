from setuptools import setup, find_packages

setup(
    name = 'keep-running',
    version = '0.0.6',
    keywords = ('keep running'),
    description = 'Keep a script or bash cmd running. Relaunch the command or script when exit.',
    license = 'MIT License',
    install_requires = [],
    scripts = ['keep-running'],
    author = 'http://www.liaohuqiu.net',
    author_email = 'liaohuqiu@gmail.com',
    url = 'https://github.com/liaohuqiu/keep-running',

    packages = find_packages(),
    platforms = 'any',
)
