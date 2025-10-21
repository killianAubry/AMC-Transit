from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="amc-transit",
    version="0.1.0",
    author="Killian Aubry",
    description="Python scripts to retrieve data from transit APIs and data sources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/killianAubry/AMC-Transit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
)
