import os
import shutil
import subprocess

tool_key = "example_tool__test_func_1"
inputs_loc = "ideas/inputs.sh"
command_loc = os.path.join("ideas", f"{tool_key}.command.sh")


def _simulate_docker():
    """simulates the docker environment"""
    if os.path.exists("ideas/"):
        shutil.rmtree("ideas/")
    print("Can I see this in github actions?")
    dirs = (
        "ideas/",
        "ideas/outputs/",
        "ideas/info/",
        "ideas/toolbox/",
        "ideas/toolbox/tools/",
    )

    for folder in dirs:
        os.makedirs(folder)

    # copy the file from a path into /ideas/toolbox/tools/
    shutil.copy(
        "ideas-toolbos-{{cookiecutter.repo_name}}/toolbox/tools/example_tool.py",
        "ideas/toolbox/tools/",
    )

    shutil.copy(
        "ideas-toolbos-{{cookiecutter.repo_name}}/function_caller.py",
        "ideas/",
    )
    shutil.copy("tests/toolbox_info.json", "ideas/info/")


def _make_command_and_inputs():
    """simulates the inputs"""
    # write the command file

    result = subprocess.run(
        ["poetry", "env", "info", "-p"],
        capture_output=True,
    )

    python_dir = result.stdout.decode().replace("\n", "")
    python_path = os.path.join(python_dir, "bin", "python")

    with open(command_loc, "w") as f:
        f.write(f"{python_path} function_caller.py {tool_key}")

    # write the inputs file
    with open(inputs_loc, "w") as f:
        f.write(
            """cell_set_file='["wow_file.isxd"]'
annotations_file='["some_file.csv"]'
"""
        )


def test_function_caller():
    """test the function caller"""

    _simulate_docker()
    _make_command_and_inputs()

    if os.path.exists(command_loc):
        print("command exists")
    else:
        print("command does not exist")

    original_dir = os.getcwd()
    os.chdir("ideas")

    result = subprocess.run(
        ["bash", f"{tool_key}.command.sh"],
        check=True,
        capture_output=True,
        text=True,
    )
    error = result.stderr
    assert error == ""
    # Check if the output file exists
    assert os.path.exists("tool_output.txt")
    with open("tool_output.txt", "r") as f:
        assert f.read() == "wow_file.isxdsome_file.csv"

    os.chdir(original_dir)

    if os.path.exists("ideas/"):
        shutil.rmtree("ideas/")
