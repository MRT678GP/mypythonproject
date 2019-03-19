from setuptools import setup, find_packages

setup(
    name='mypythonproject',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Build a Package Project',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/MRT678GP/mypythonproject.git',
    author='Thato Mokoka',
    author_email='tmokoka90@gmail.com'
)
