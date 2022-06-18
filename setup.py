from setuptools import setup
from typing import List


# declaring variables for setup
project_name = "housing-predictor"
version = "0.0.1"
author = "Vyankatesh"
description = "This is first project in ineuron"
packages = ["housing"]
requirement_file_name = 'requirements.txt'

def get_requirements_list()->List[str]:
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
packages = packages,
install_requires = get_requirements_list(),
requirement_file_name  = requirement_file_name


)

