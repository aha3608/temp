from configparser import ConfigParser

# Load the INI file
config = ConfigParser()
config.read('info.ini')

# Function to get values based on environment
def get_config(environment, key):
    if environment in config:
        return config[environment].get(key, None)
    else:
        raise ValueError(f"Environment '{environment}' not found in the config file.")

# Example usage
dev_value = get_config('dev', 'variable_name')  # Replace 'variable_name' with your key
prd_value = get_config('prd', 'variable_name')

print(f"Dev Value: {dev_value}")
print(f"Prod Value: {prd_value}")
