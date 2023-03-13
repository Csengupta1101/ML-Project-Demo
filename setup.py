''' This is the set up file  , we will import package and setup modules here'''
 from setuptools import find_packages,setup

''' Here we are describing the project details along with it's initial version within the setup module'''
setup(
 name = 'mldemo',
 version='0.0.1',
 author='Chandan',
 author_email='csengupta1101@outlook.com',
 packages=find_packages())