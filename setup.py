from setuptools import setup, find_packages


with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    

setup(
    name='ml_ops_bootcamp',
    version='0.1.0',
    description='Machine Learning Operations Bootcamp',
    author='Chandan D. Chaudhari',
    author_email='chaudhari.chandan22@gmail.com',
    url='https://github.com/chandanc5525/ML_OPS-BootCamp',
    packages=find_packages(),
    install_requires=requirements,)
