import ruamel.yaml
import logging
import sys
import os

# Initialize YAML object with round-trip to preserve formatting + comments
yaml = ruamel.yaml.YAML(typ='rt')
yaml.preserve_quotes = True

# Set up logging configuration
def setup_logging(level=logging.INFO):
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Load .yaml files
def load_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return yaml.load(f)
    
    except FileNotFoundError:
        logging.error(f"Unable to find the file: {filepath}. Please check the file path and try again.")
        sys.exit(1)
    
    except PermissionError:
        logging.error(f"Permission denied when trying to read the file: {filepath}. Please check your file permissions.")
        sys.exit(1)

# Write updated data back to a YAML file
def write_yaml_file(filepath, data):
    try:
        with open(filepath, 'w+') as w:
            yaml.dump(data, w)
    except PermissionError as e:
        logging.error(f"Permission error: {e}")
        sys.exit(1)

#standard merge - 1) keep the original keys and change to new values 2)erase old values in original
#force merge = true - change the original values but do not add any new ones no removal
#full merge  = true - add or change any values to match the new file
    
#defining a function to merge the two files together
def merge(orig_data, new_data, force_update = False, full_update = False):
    #full_update allows for the entire file to be rewritten to copy over any changes 
    #from the new file into the old file
    if full_update:
        orig_data.clear()
        orig_data.update(new_data)
    
    #force update only allows for existing keys to be updated from the new file
    #does not add or remove any existing keys from the file 
    elif force_update:
        for key in list(orig_data):
            if key in new_data:
                if isinstance(orig_data[key], dict) and isinstance(new_data[key], dict):
                    merge(orig_data[key], new_data[key], force_update= True)
                else:
                    orig_data[key] = new_data[key]
    
    else: 
       #both flags are false
       #adds new keys, updates the existing, and removes the unused keys from new file
        for key, value in new_data.items():
            if key in orig_data and isinstance(orig_data[key], dict) and isinstance(new_data,dict):
                merge(orig_data[key],value)

            else:
                orig_data[key] = value

        #removal of old varaibles from original file
        for key in list(orig_data):
            if key not in new_data:
                del orig_data[key]
    