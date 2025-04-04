import yaml
import pandas as pd
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

        # Open the Excel file and process each tab
        for tab_name, cells in tabs.items():
            df = pd.read_excel(file_path, sheet_name=tab_name)
            extracted_data[file_name][tab_name] = []

            # Extract data points based on 'cell' and 'label'
            for cell_info in cells:
                cell_value = df.loc[df['cell'] == cell_info.get('cell'), 'label'].values
                if cell_value.size > 0:
                    extracted_data[file_name][tab_name].append({
                        'cell': cell_info.get('cell'),
                        'label': cell_value[0]
                    })

    return extracted_data


# Example usage
if __name__ == "__main__":
    # Path to the config.yml file
    config_path = "config.yml"

    # Extract data from the Excel files based on the config
    data = parse_config_and_extract_data(config_path)

    # Print the extracted data
    print(data)
