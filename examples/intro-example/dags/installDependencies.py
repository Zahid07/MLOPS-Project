# open requirements.txt and install all packages
import pip

def install_packages():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    for package in requirements:
        pip.main(['install', package])