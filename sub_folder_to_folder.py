import os
import shutil

def copy_images_to_directory(source_directory, target_directory):
    """
    Copies image files from subdirectories within the source directory to a target directory.

    Args:
    source_directory (str): The path to the directory containing subdirectories of images.
    target_directory (str): The path to the directory where images will be copied.
    """
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)  # Create the target directory if it doesn't exist

    for subdir in os.listdir(source_directory):
        subdir_path = os.path.join(source_directory, subdir)
        if os.path.isdir(subdir_path):  # Check if it's a directory
            for file in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, file)
                if os.path.isfile(file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    shutil.copy(file_path, target_directory)  # Copy file

# Example usage
source_directory = '/home/achazhoor/Documents/2024/detr_trial_1/neu_data/NEU-DET/validation/images'
target_directory = '/home/achazhoor/Documents/2024/detr_trial_1/annotation_neu/val_images'
copy_images_to_directory(source_directory, target_directory)
