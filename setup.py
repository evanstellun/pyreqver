from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="python-version-selector",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to find Python versions that support all libraries in requirements.txt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-version-selector",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "python-version-selector=main:main",
        ],
    },
)