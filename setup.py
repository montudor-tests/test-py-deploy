import os
from setuptools import (
	find_packages,
	setup,
)

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='montudor-test-repo',
    packages=find_packages(),
    version='0.0.5',
    description='A regular hello world library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Monte Hellawell',
    author_email='monte@montudor.com',
    url='https://github.com/montudor/test-py-deploy',
    download_url='https://github.com/montudor/test-py-deploy/archive/v0.0.5.tar.gz',
    keywords=[],
    classifiers=[]
)
