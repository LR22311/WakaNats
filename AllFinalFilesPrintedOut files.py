import csv,os

keyword = "Final" #The keyword word we are looking for in the file
my_dir = r"C:\Users\lr817\Desktop\WakaNats\CSV files for WakaNats\WakaNats2017" #The directory which contains our files

print("**start print**")
for root_dir_path, sub_dirs, files in os.walk(my_dir):
    matching_files = [file for file in files if keyword in file]
    for file_name in matching_files:
        file_path = os.path.join(root_dir_path, file_name)
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line)
print("**********End Print********")
