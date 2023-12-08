# Template for toolboxes in IDEAS

This cookiecutter template allows you to create toolboxes
that are compatible with IDEAS using the latest (circa 2023)
infrastructure and idioms. 

## Usage

Typically, you will never have to interact with this, 
as the [toolbox creator app](https://github.com/inscopix/toolbox-creator) will use this internally.

If you want to use this directly (and not use the app), then
do the following:

```bash
cookiecutter https://github.com/inscopix/ideas-toolbox-new-template
```

## Installing

Don't.

You don't have to install this unless you're developing this. 


## Developing 

### Install

Install using poetry:

```bash
poetry install
```

### Run tests

```bash
make test
make test-docker
```

