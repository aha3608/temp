import os

def append_string_to_files(directory, input_string):
    """
    Appends the input string to all files in the given directory.

    Args:
        directory (str): Path to the directory containing the files.
        input_string (str): The string to append to each file.

    Returns:
        None
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Iterate through all files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Check if it's a file (not a subdirectory)
        if os.path.isfile(file_path):
            try:
                # Open the file in append mode and add the input string
                with open(file_path, 'a') as file:
                    file.write(input_string)
                print(f"Appended string to: {file_name}")
            except Exception as e:
                print(f"Error appending to {file_name}: {e}")

if __name__ == "__main__":
    # Example usage
    directory_path = "path/to/your/directory"
    string_to_append = "\nThis is the appended string."

    append_string_to_files(directory_path, string_to_append)

