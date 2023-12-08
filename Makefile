# global variables
IDEAS_GITHUB_TOKEN_FILE=.ideas-github-token
TOOLBOX_DIR="../ideas-toolbox-my-toolbox/"
TOOL_KEY="example_tool__test_func_1"

.PHONY:  test verify-github-token



verify-github-token:
	@echo "Verifying GitHub token"
ifneq ($(shell test -f ${IDEAS_GITHUB_TOKEN_FILE} && echo yes),yes)
	$(error The GitHub token file ${IDEAS_GITHUB_TOKEN_FILE} does not exist)
endif

test: verify-github-token
	@echo "Testing function caller in a docker container..."
	@-rm -rf $(TOOLBOX_DIR)
	@cookiecutter . --no-input --output-dir ../
	@cp .ideas-github-token $(TOOLBOX_DIR)
	@cp tests/inputs/$(TOOL_KEY).json $(TOOLBOX_DIR)inputs/
	@cp tests/toolbox_info.json $(TOOLBOX_DIR)info/toolbox_info.json
	@cp tests/commands/$(TOOL_KEY).sh $(TOOLBOX_DIR)commands/
	@chmod a+x $(TOOLBOX_DIR)commands/$(TOOL_KEY).sh 
	@echo "Making toolbox_info.json..."
	@cd $(TOOLBOX_DIR); git init; git add -A .; git commit -m "initial commit"; git tag "1.2.3"; make toolbox-info
	@echo "Going to toolbox folder and running command..."
	@cd $(TOOLBOX_DIR); make run TOOL="$(TOOL_KEY)"
	@bash check_tool_output.sh
