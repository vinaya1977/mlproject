from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e.'
def get_requirements(file_path:str)->List[str]:
    "'this is a requirement file redaer'"
    
    
    requirements = []
    with open(file_path, 'r') as file:
        for line in file:
            requirements.append(line.strip())

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Vipin',
author_email='vj90034@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)


