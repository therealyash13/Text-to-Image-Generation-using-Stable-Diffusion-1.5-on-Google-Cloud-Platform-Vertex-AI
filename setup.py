                                                                                          
from setuptools import setup

setup(
    name="generate_images",
    version="1.0",
    py_modules=["cli_app"],
    install_requires=[
        "diffusers",  # List other required packages here
    ],
    entry_points={
        "console_scripts": [
            "generate=cli_app:main",
        ],
    },
)




