# yaml-updater

Description:

This project provides a Python-based tool for merging YAML files. It allows users to update an existing YAML file with values from a new YAML file, with options for force updating or fully updating the entire file.

Installation:

Before running this script, ensure you have Python installed on your system. This project requires the ruamel.yaml package to handle YAML files efficiently while preserving comments and formatting.

Dependencies

    Python 3.x
    ruamel.yaml

Installing Dependencies
Install the required Python package using pip:

>pip install ruamel.yaml

Usage:

The project consists of two main files: update.py and main.py. update.py contains the logic for merging YAML files, while main.py is the entry point for the user to execute the merge process.

For merging to take place the two files must be located inside the folder downloaded from the github repo

follow the steps printed to the terminal by typing the name of the files you want to merge
    Force Update (y/n): Updating existing keys without adding new ones.
    Full Update (y/n): Overwriting the original file with the new file's content, including adding new keys and updating existing ones.

example: 
![image](https://github.com/ThreeLeftTurns/yaml-updater/assets/34759970/4b7728ab-d081-48db-8b28-872abe882119)

User under your own discression
