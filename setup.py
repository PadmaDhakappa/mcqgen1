from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Padma Dhakappa',
    author_email='dhakappa.padma@gmail.com',
    install_requires=['openai','PyPDF2','langchain','streamlit','python-dotenv'],
    packages=find_packages()
)