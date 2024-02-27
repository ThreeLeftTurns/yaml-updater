from update import *


if __name__ == "__main__":

    setup_logging()
    #saves the output file to the folder the script is living
    file_directory = os.path.dirname(os.path.abspath(__file__))
    output_filename = "output.yaml"  # Specify your output filename here
    
    output_file_path = os.path.join(file_directory, output_filename)

    #prompt user for file name of the original yaml file
    input_file_path = input("Enter the path to the original YAML file: ")
    orig_data = load_file(input_file_path)

    #prompt user for the file name of the new yaml file
    new_data_path = input("Enter the path to the new YAML file for merging: ")
    new_data = load_file(new_data_path)      

    #setting flags for function
    userinput0 = input("force_update? y/n").lower()
    if userinput0 in ['yes', 'y']:
        force_update = True
    
    else:
        force_update = False

    #setting flags for function
    userinput1 = input("full_update? y/n").lower()
    if userinput0 in ['yes', 'y']:
        full_update = True

    else:
        full_update = False

    # Perform merging; adjust force_update and full_update as needed
    merge(orig_data, new_data, force_update = userinput0, full_update= userinput1)

    # Write the merged data to the output file
    write_yaml_file(output_file_path, orig_data)
    print("file was saved under: {file_directory}")