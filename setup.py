from setuptools import setup, find_packages

setup(
    name="cencus-income",
    version="0.0.1",  # giving version to my package
    author="sawan",
    author_email="sawan.gomia@gmail.com",
    packages=find_packages(), # it will find the package from project folder
    install_requires=["pandas","numpy","flask"]
)