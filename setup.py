from setuptools import setup, find_packages

setup(
    name='pysearch',
    version='1.0.0',
    author='A. Buschinneli',
    author_email='cat.me.pentest@gmail.com',
    packages=find_packages(),
    install_requires=[
        'simple_chalk',
        'requests_html',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'pysearch = pysearch.pysearch:main'
        ]
    }
)