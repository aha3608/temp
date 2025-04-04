import yaml
import openpyxl
import os

def parse_config_and_extract_data(config_path):
    # Load the YAML configuration file
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

    extracted_data = {}

    # Iterate through files and tabs in the config
    for file_name, tabs in config.get('files', {}).items():
        file_path = os.path.join(config.get('location', ''), f"{file_name}.xlsx")
        extracted_data[file_name] = {}

        # Load the Excel workbook
        workbook = openpyxl.load_workbook(file_path)

        for tab_name, cells in tabs.items():
            worksheet = workbook[tab_name]
            extracted_data[file_name][tab_name] = []

            # Extract data from specified cell locations
            for cell_info in cells:
                cell_location = cell_info.get('cell')
                label = worksheet[cell_location].value  # Read value directly from the cell
                extracted_data[file_name][tab_name].append({
                    'cell': cell_location,
                    'label': label
                })

    return extracted_data


# Example usage
if __name__ == "__main__":
    # Path to the config.yml file
    config_path = "config.yml"

    # Extract data from Excel files based on the config
    data
