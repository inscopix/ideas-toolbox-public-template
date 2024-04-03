"""setup file"""
import os

from setuptools import setup

# make sure this is set using
# export IDEAS_GITHUB_TOKEN=$(cat .ideas-github-token)
# just setting it won't work
token = os.environ["IDEAS_GITHUB_TOKEN"]

install_requires = []
if os.path.isfile("user_deps.txt"):
    with open("user_deps.txt") as f:
        install_requires = f.read().splitlines()

setup(
    name="ideas-toolbox-{{cookiecutter.repo_name}}",
    python_requires=">=3.9",
    version="1.0.0",
    packages=[],
    description="",
    url="https://github.com/inscopix/ideas-toolbox-{{cookiecutter.repo_name}}",
    install_requires=[
        f"ideas-python-utils@git+https://{token}@github.com/inscopix/ideas-python-utils.git@10.4.1",
        f"ideas-commons@git+https://{token}@github.com/inscopix/ideas-commons.git@1.8.0",
        f"ideas-tools-profiler@git+https://{token}@github.com/inscopix/ideas-tools-profiler.git@0.1.0",
        "isx==1.0.3",
        "requests==2.27.1",  # required by BE
        "urllib3==1.26.16",
        "configobj==5.0.8",
        "pytest==7.4.2",
        "tabulate==0.9.0",
    ]
    + install_requires,
)
