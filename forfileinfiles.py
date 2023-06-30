import os

keyword = "Final"

my_dir = r"C:\Users\lr817\Desktop\WakaNats\CSV files for WakaNats\WakaNats2017"


for root_dir_path, sub_dirs, files in os.walk(my_dir):      
    print("Root Directory Path:", root_dir_path)
    print('Sub Directories:', sub_dirs)
    matching_files = [file for file in files if keyword in os.path.join(root_dir_path, file)]
    if matching_files:
        print('Files:', matching_files)