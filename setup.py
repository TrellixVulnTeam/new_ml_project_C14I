from setuptools import setup, find_packages
from typing import List


# declaring variables for setup
project_name = "housing-predictor"
version = "0.0.1"
author = "Vyankatesh"
description = "This is first project in ineuron"
packages = ["housing"]
requirement_file_name = 'requirements.txt'

def get_requirements_list()->List[str] # List[str] it shows what the function returns when it is triggered: 
    """
    This function is going to return list which contain name of libraries mentioned in the requirements.txt fiel

    """
    with open(requirement_file_name) as requirement_file:
        return requirement_file.readlines()


setup(

name = project_name,
version = version,
author = author,
description = description,
packages = packages, # find_packages()
install_requires = get_requirements_list(), # to install external packages like sklearn, pandas etc
requirement_file_name  = requirement_file_name


)

# find packages will find all local packages(folder) whereever there __init__ file and try to install
# -e . is also do the same thing as find packages function if you use this method we must need setup.py file