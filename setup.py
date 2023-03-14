''' This is the set up file  , we will import package and setup modules here'''
from setuptools import find_packages , setup
from typing import List

''' Hypen e variable created separately as a variable and "-e ." is taken as a value inside of it so that this partular object can stay in the requirements.txt file and can trigger the setup 
python file but will not impact our main code '''

hypen_e = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        ''' The issue with the readlines statement is that as it goes into the requirements file , it will read lines separately with \n block inside of it , however with the help of list 
        comprehension as below we can replace the "\n" block with blank'''
        requirements = [req.replace("\n","")for req in requirements]
        ''' This if block will ensure that whenever the set up file calls for the requirements.txt file for module installation , the '-e .' block remains ignored'''
        if hypen_e in requirements:
            requirements.remove(hypen_e)
    return requirements




''' Here we are describing the project details along with it's initial version within the setup module'''
setup(
 name = 'mldemo',
 version='0.0.1',
 author='Chandan',
 author_email='csengupta1101@outlook.com',
 packages=find_packages(),
 install_requires = get_requirements('requirements.txt')
 )