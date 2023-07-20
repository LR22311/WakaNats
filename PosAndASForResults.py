import os
import csv

keyword = 'Final'
My_Dir = r'lif Files for WakaNats\WakaNats2018'
Out_File = 'FinalResults.csv'

unordered_data = []  # List to store column 1 and 2s data
points_dict = {}  # Dictionary to store AS values and their corresponding points

for root, sub_dirs, files in os.walk(My_Dir):
    Final_Files = (file for file in files if keyword in file)
    for file_name in Final_Files:
        New_Path = os.path.join(root, file_name)  # This part finds the files with the keyword "Final"
        with open(New_Path, 'r') as Raw_Results:
            csv_reader = csv.reader(Raw_Results)
            next(csv_reader)  # This code skips the title so it doesn't print it into the file we opened
            for line in csv_reader:
                unordered_data.append((line[0], line[5]))  # appended the data into our List

sorted_data = sorted(unordered_data, key=lambda x: x[1])  # Sort the data by column 6 in alphabetical order


def assign_points(rank):
    # Function to assign points based on the rank
    if rank == '':
        return 0
    rank = int(rank)
    if rank == 1:
        return 8
    elif rank == 2:
        return 7
    elif rank == 3:
        return 6
    elif rank == 4:
        return 5
    elif rank == 5:
        return 4
    elif rank == 6:
        return 3
    elif rank == 7:
        return 2
    else:
        return 1


with open(Out_File, "w", newline="") as output_csv:
    csv_writer = csv.writer(output_csv)  # This part is used to open up the file where we will write the data needed for the assessment
    csv_writer.writerow(['Pos', 'AS', 'Points'])  # Names of the columns
    for line in sorted_data:
        position = line[0]
        as_value = line[1]
        points = assign_points(position)
        if as_value not in points_dict:
            points_dict[as_value] = points
        else:
            points_dict[as_value] += points

    # Writing the data with the points assigned
    for as_value, points in points_dict.items():
        csv_writer.writerow(['', as_value, points])
