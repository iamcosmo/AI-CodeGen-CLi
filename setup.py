import os
from setuptools import setup, find_packages

setup(
    name="AI-CodeGen-CLi",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "google-generativeai",
        "python-dotenv",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "codegen=codegen.codegen:main"
        ]
    },
    author="Chandan(Cosmos)",
    description="A CLI AI-powered Code Generator using Gemini API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iamcosmo/AI-CodeGen-CLi.git",
)

# Run post-install script
os.system("python post_install.py")