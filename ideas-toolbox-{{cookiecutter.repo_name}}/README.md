# ideas-toolbox-{{cookiecutter.repo_name}}

**Table of Contents**
- [Toolbox Description](#toolbox-description)
- [Navigating the Project Repository](#navigating-the-project-repository)
- [Usage Instructions](#usage-instructions)
  - [Setup the development environment](#setup-the-development-environment)
  - [List available commands](#list-available-commands)
  - [Build Docker image](#build-docker-image)
  - [Clean project](#clean-project)
  - [Run a specific tool](#run-a-specific-tool)
  - [Run jupyterlab inside the docker container](#run-jupyterlab-inside-the-docker-container)
  - [Run tests](#run-tests)
  - [Generate toolbox summary](#generate-toolbox-summary)

## Toolbox Description
IDEAS toolbox for {{cookiecutter.toolbox_name}}.

## Navigating the Project Repository

```
├── commands                # Standardized scripts to execute tools on the cloud
├── data                    # Small data files used for testing
├── info                    # Files describing the toolbox & tools for the IDEAS system
├── inputs                  # Predefined test inputs for the command scripts
│── toolbox                 # Contains all code for running and testing the tools
│   ├── tools               # Contains the individual analysis tools
│   ├── utils               # General utilities used by the tools
│   ├── tests               # Unit tests for the individual tools
└── .gitignore              # Tells Git which files & folders to ignore
│── Dockerfile              # Commands to assemble the Docker image
│── Makefile                # To automate and standardize toolbox usage
│── check_tool.sh           # Checks if tool is valid before execution
│── function_call.py        # Executes tool for IDEAS system
│── pyproject.toml          # Configuration for the python project
│── setup.py                # Specifies dependencies of the python project
│── user_deps.txt           # Specifies user dependencies of the python project
```

## Usage Instructions

### Set up the development environment
- Ensure you have the following development dependencies installed:
    - Docker
    - make
- Under the `ideas-toolbox-{{cookiecutter.repo_name}}` repository, create a file called `.ideas-github-token` containing a valid GitHub token that has sufficient permissions to access this repository and its dependencies.

### List available commands
```
make help
```

### Build Docker image
```
make build
```

### Clean project
```
make clean
```

### Run a specific tool
```
make run TOOL=tool_name
```

### Run jupyterlab inside the docker container
```
make run-jupyter
```

and navigate to http://localhost:8888 to get a Jupyter environment inside the docker container 

### Run tests
```
make test
```

Test arguments can be specified using `TEST_ARGS` as shown below. Refer to [pytest documentation](https://docs.pytest.org/en/7.1.x/how-to/usage.html) for supported arguments.
```
make test TEST_ARGS="-k TestWorkflows"
```

### Generate toolbox summary
This will generate a json summary of the toolbox including tools, parameters, hardware requirements, 
versions, etc.
```
make toolbox-info
```