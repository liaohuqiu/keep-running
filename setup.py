from setuptools import setup, find_packages

setup(
    name = 'keep-running',
    version = '0.0.3',
    keywords = ('keep running'),
    description = '',
    license = 'MIT License',
    install_requires = [],
    scripts = ['bin/keep-running'],
    author = 'http://www.liaohuqiu.net',
    author_email = 'liaohuqiu@gmail.com',
    url = 'https://github.com/liaohuqiu/python-keep-running',

    packages = find_packages(),
    platforms = 'any',
)
