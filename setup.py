# This is file is basically used for creating our ML models as packages. So that these packages can be deployed anywhere & can be used by anyone.

from setuptools import find_packages,setup
from typing import List


# 'Find_packages' used for getting all the packages being used in the whole directory. It will actually search for the folders which have the "__init__.py file in it & will install the packages present in that particular folders".

# The 'setup.py' file is at the heart of a Python project. It describes all the metadata about your project. There are quite a few fields you can add to a project to give it a rich set of metadata describing the project. However, there are only three required fields: name, version, and packages. The name field must be unique if you wish to publish your package on the Python Package Index (PyPI). The version field keeps track of different releases of the project. The package’s field describes where you’ve put the Python source code within your project.

HYPHEN_E_DOT = '-e .'
# This 'HYPHEN_E_DOT' written in requirements.txt indicates that while installing the modules from the 'requirements.txt', the 'setup.py' file should also start building the packages.

def get_requirements(filepath:str) -> List[str]:
    # This function returns the list of requirements...

    requirements=[]
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        # The readlines function will also read the next line character "\n". So, to avoid this we replaced it with an empty character.

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='end_to_end_mlproject',
    version='0.0.1',
    author='Vedansh',
    author_email='vedanshgupta606@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)