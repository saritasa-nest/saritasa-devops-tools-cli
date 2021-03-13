import sys

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRES = [
    "setuptools>=42",
    "wheel",
    "boto3==1.17.22",
    "emoji==1.2.0",
    "prompter==0.3.10",
    "invoke==1.5.0",
    "click==7.1.2",
    "termcolor==1.1.0",
    "rich==9.13.0",
    "mitmproxy==6.0.2",
    "msgpack==1.0.2",
    "redis==3.5.3",
    "inflection==0.5.1",
    "psutil==5.8.0",
    "funcy==1.15",
    "toolz==0.11.1",
    "more-itertools==8.7.0",
    "fn==0.4.3",
]

setup(
    name="marina",  # Replace with your own username
    version="0.0.1",
    author="Dmitry Semenov",
    author_email="dmitry@saritasa.com",
    description="Devops tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saritasa-nest/saritasa-devops-tools-cli",
    project_urls={
        "Bug Tracker": "https://github.com/saritasa-nest/saritasa-devops-tools-cli/issues",
    },
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    entry_points={"console_scripts": ["marina = marina.main:cli"]},
    classifiers=[
        "Development Status :: 5 - Production/Alpha",
        "Environment :: Console",
        "Intended Audience :: Saritasa Devops",
        "Intended Audience :: Saritasa System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Systems Administration",
    ],
)
