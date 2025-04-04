import yaml

def parse_config_and_extract_data(config_path):
    # Load the YAML configuration file
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

    extracted_data = {}

    # Iterate through the files and tabs in the config
    for file_name, tabs in config.get('files', {}).items():
        extracted_data[file_name] = {}
        for tab_name, cells in tabs.items():
            extracted_data[file_name][tab_name] = []
            for cell_info in cells:
                extracted_data[file_name][tab_name].append({
                    'cell': cell_info.get('cell'),
                    'label': cell_info.get('label')
                })

    return extracted_data


# Example usage
if __name__ == "__main__":
    # Path to the config.yml file
    config_path = "config.yml"

    # Extract data from the config file
    data = parse_config_and_extract_data(config_path)

    # Print the extracted data
    print(data)

