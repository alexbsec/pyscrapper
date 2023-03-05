from setuptools import setup, find_packages

setup(
    name='pyscrapper',
    version='1.0.0',
    author='A. Buschinneli',
    author_email='cat.me.pentest@gmail.com',
    packages=find_packages(),
    install_requires=[
        'fake_useragent',
        'simple_chalk',
        'requests_html',
        'urllib',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'pyscrapper = pyscrapper.googlesearch:main'
        ]
    }
)