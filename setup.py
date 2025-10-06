from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "MLOPS_Hotel_Reservation",
    version= "1",
    author = "Yash N Padhye",
    packages= find_packages(),
    install_requires = requirements

)