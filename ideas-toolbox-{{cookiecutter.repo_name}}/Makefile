# toolbox variables
REPO=inscopix
PROJECT=ideas
MODULE=toolbox
IMAGE_NAME={{cookiecutter.repo_name}}
VERSION=$(shell git describe --tags --always --dirty)
IMAGE_TAG=${REPO}/${PROJECT}/${MODULE}/${IMAGE_NAME}:${VERSION}
FULL_NAME=${REPO}/${PROJECT}/${MODULE}/${IMAGE_NAME}
CONTAINER_NAME=${REPO}-${PROJECT}-${MODULE}-${IMAGE_NAME}-${VERSION}
PLATFORM=linux/amd64

# jupyter-lab configurations
ifndef JUPYTERLAB_PORT
	JUPYTERLAB_PORT=8889
endif


# this flag determines whether files should be 
# dynamically renamed (if possible) after function 
# execution. 
# You want to leave this to true so that static 
# filenames are generated, so that these can be 
# annotated by the app. 
# If you want to see what happens on IDEAS, you can
# switch this to false 
ifndef TC_NO_RENAME
	TC_NO_RENAME="true"
endif



# credentials
IDEAS_GITHUB_TOKEN_FILE=.ideas-github-token

# profiler
ifndef IDEAS_PROFILER
	IDEAS_PROFILER=0
endif

ifeq ($(IDEAS_PROFILER),1)
define run_command
    bash -c 'mkdir -p "/ideas/outputs/$1" \
        && cd "/ideas/outputs/$1" \
        && cp "/ideas/inputs/$1.json" "/ideas/outputs/$1/inputs.json" \
        && ( ideas-tools-profiler & "/ideas/commands/$1.sh" ) \
	    && rm "/ideas/outputs/$1/inputs.json"'
endef
else
define run_command
    bash -c 'mkdir -p "/ideas/outputs/$1" \
        && cd "/ideas/outputs/$1" \
        && cp "/ideas/inputs/$1.json" "/ideas/outputs/$1/inputs.json" \
        && "/ideas/commands/$1.sh" \
	    && rm "/ideas/outputs/$1/inputs.json"'
endef
endif



.PHONY: help verify-github-token build jupyter test clean


.DEFAULT_GOAL := build

clean:
	@echo "Cleaning up"
	-docker rm $(CONTAINER_NAME)
	-docker images | grep $(FULL_NAME) | awk '{print $$1 ":" $$2}' | grep -v $(VERSION) | xargs docker rmi


verify-github-token:
	@echo "Verifying GitHub token"
ifneq ($(shell test -f ${IDEAS_GITHUB_TOKEN_FILE} && echo yes),yes)
	$(error The GitHub token file ${IDEAS_GITHUB_TOKEN_FILE} does not exist)
endif


build: verify-github-token
	@echo "Building docker image..."
	DOCKER_BUILDKIT=1 docker build . -t $(IMAGE_TAG) \
		--platform ${PLATFORM} \
		--target base \
		--secret id=ideas_github_token,src=${IDEAS_GITHUB_TOKEN_FILE}


jupyter: verify-github-token clean
	@echo "Launching container with Jupyter lab..."
	DOCKER_BUILDKIT=1 docker build . -t $(IMAGE_TAG)-jupyter \
		--platform ${PLATFORM} \
		--target jupyter \
		--secret id=ideas_github_token,src=${IDEAS_GITHUB_TOKEN_FILE}
	docker run -ti \
			-v $(PWD)/commands:/ideas/commands \
			-v $(PWD)/data:/ideas/data \
			-v $(PWD)/inputs:/ideas/inputs \
			-v $(PWD)/notebooks:/ideas/notebooks \
			-v $(PWD)/outputs:/ideas/outputs \
			-v $(PWD)/toolbox:/ideas/toolbox \
			-p ${JUPYTERLAB_PORT}:${JUPYTERLAB_PORT} \
			-e JUPYTERLAB_PORT=$(JUPYTERLAB_PORT) \
			--name $(CONTAINER_NAME) \
	    $(IMAGE_TAG)-jupyter \
	    jupyter-lab --ip 0.0.0.0 --port $(JUPYTERLAB_PORT) --no-browser --allow-root --NotebookApp.token="" \
	&& docker rm $(CONTAINER_NAME)

test: build clean 
	@echo "Running toolbox tests..."
	-mkdir -p $(PWD)/outputs
	docker run \
		--platform ${PLATFORM} \
		-v $(PWD)/data:/ideas/data \
		-v $(PWD)/outputs:/ideas/outputs \
		-v $(PWD)/inputs:/ideas/inputs \
		-v $(PWD)/commands:/ideas/commands \
		-w /ideas \
		-e CODEBUILD_BUILD_ID=${CODEBUILD_BUILD_ID} \
		-e IDEAS_GITHUB_TOKEN=$(shell cat ${IDEAS_GITHUB_TOKEN_FILE}) \
		--name $(CONTAINER_NAME) \
		${IMAGE_TAG} \
		pytest $(TEST_ARGS) 
	
toolbox-info:
	@echo "Copying toolbox_info.json and inserting version number..."
	@-mkdir -p $(PWD)/toolbox/tests/outputs
	@jq '.version = "$(VERSION)"' info/toolbox_info.json > $(PWD)/toolbox/tests/outputs/toolbox_info.json 



run: build clean
	@bash check_tool.sh $(TOOL)
	@echo "Running the  $(TOOL) tool in a Docker container. Outputs will be in /outputs/$(TOOL)"
	-rm -rf $(PWD)/outputs/
	docker run \
			--platform ${PLATFORM} \
			-v $(PWD)/data:/ideas/data \
			-v $(PWD)/inputs:/ideas/inputs \
			-v $(PWD)/commands:/ideas/commands \
			-e TC_NO_RENAME=$(TC_NO_RENAME) \
			--name $(CONTAINER_NAME) \
	    $(IMAGE_TAG) \
		$(call run_command,$(TOOL)) \
	&& docker cp $(CONTAINER_NAME):/ideas/outputs $(PWD)/outputs \
	&& docker rm $(CONTAINER_NAME)
