#This file was created so that it could take the file
#directory and then list all the files into a text file



import os

def list_files_in_directory(directory_path, output_file):
    """
    Writes all the paths within the specified directory to a text file.

    Args:
    directory_path (str): The directory path to list files from.
    output_file (str): The output file path where the directory paths will be saved.
    """
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(directory_path):
            for name in files:
                file_path = os.path.join(root, name)
                file.write(file_path + '\n')
            for name in dirs:
                dir_path = os.path.join(root, name)
                file.write(dir_path + '\n')

# Example usage
directory_path = '/home/achazhoor/Documents/2024/detr_trial_1/neu_data/NEU-DET/validation/annotations'  # Replace with your directory path
output_file = '/home/achazhoor/Documents/2024/detr_trial_1/annotation_neu/output_val.txt'  # The text file where the paths will be written
list_files_in_directory(directory_path, output_file)
