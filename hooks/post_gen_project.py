"""tasks to perform after project generation"""


import os
import shutil

empty_folders = (
    "commands",
    "inputs",
    "outputs",
    "resources",
)

for folder in empty_folders:
    os.mkdir(folder)

# copy the simple dockerfile into dockerfile
# so that by default we don't use IDPS
shutil.copy("Dockerfile.simple", "Dockerfile")
