import configparser

def load_ini_values(file_path):
    # Create a ConfigParser object
    config = configparser.ConfigParser()
    
    # Read the .ini file
    config.read(file_path)
    
    # Load all values into the `info` dictionary
    info = {section: dict(config.items(section)) for section in config.sections()}
    
    return info

# Example usage
file_path = 'config.ini'
info = load_ini_values(file_path)
print(info)

