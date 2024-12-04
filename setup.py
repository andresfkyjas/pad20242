from setuptools import setup, find_packages

setup(
    name='actividad',
    version='0.1.0',
    packages=find_packages(),
    python_requires= '>3.9',
    platforms=['any'],
    install_requires=[
        'pandas',
        'selenium==4.11.2',
        'webdriver-manager==4.0.2'
    ]
)