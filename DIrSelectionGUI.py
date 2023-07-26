import os,csv
import tkinter as tk

root= tk.Tk()

root.geometry("500x500")
root.title("WakaNats")


def assign_points(Points):
    # Function to assign Points based on the rank
    if Points == '':
        return 0
    Points =int(Points)
    if Points == 1:
        return 8
    elif Points == 2:
        return 7
    elif Points == 3:
        return 6
    elif Points == 4:
        return 5
    elif Points == 5:
        return 4
    elif Points == 6:
        return 3
    elif Points == 7:
        return 2
    else:
        return 1

def Process_2018():
    Keyword = 'Final'
    My_Dir = r'lif Files for WakaNats\WakaNats2018'
    Out_File = 'Final Results\FinalResultsOf2018.csv'
    Data = []  # List to store column 1 and 2s data
    Points_Dict = {}  # Dictionary to store AS values and their corresponding Points

    for root, sub_dirs, files in os.walk(My_Dir):
        Final_Files = (file for file in files if Keyword in file)
        for file_name in Final_Files:
            New_Path = os.path.join(root, file_name)  # This part finds the files with the keyword "Final"
            with open(New_Path, 'r') as Raw_Results:
                csv_reader = csv.reader(Raw_Results)
                next(csv_reader)  # This code skips the title so it doesn't print it into the file we opened
                for line in csv_reader:
                    # Check if column 2 (AS value) is not empty before appending the data
                    if line[5].strip():  # Strip whitespace to handle any leading/trailing spaces
                        Data.append((line[0], line[5]))  # Appended the data into our List

    for line in Data:
        position, AS_Value = line
        Points = assign_points(position)
        if AS_Value not in Points_Dict:
            Points_Dict[AS_Value] = Points
        else:
            Points_Dict[AS_Value] += Points

    # Sort the Points_Dict in descending order of points
    sorted_points_dict = dict(sorted(Points_Dict.items(), key=lambda item: item[1], reverse=True))

    # Write the sorted data to the CSV file
    with open(Out_File, "w", newline="") as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(['Points', 'Association Name'])  # Names of the columns
        for AS_Value, Points in sorted_points_dict.items():
            csv_writer.writerow([Points, AS_Value])


def Process_2017():
    Keyword= 'Final'
    My_Dir = r'lif Files for WakaNats\WakaNats2017'
    Out_File = 'Final Results\FinalResultsOf2017.csv'
    Data = [] #List to store column 1 and 2s data
    Points_Dict = {} ## Dictionary to store AS values and their corresponding Points


    for root, sub_dirs, files in os.walk(My_Dir):
        Final_Files = (file for file in files if Keyword in file)
        for file_name in Final_Files:
            New_Path = os.path.join(root, file_name)  # This part finds the files with the keyword "Final"
            with open(New_Path, 'r') as Raw_Results:
                csv_reader = csv.reader(Raw_Results)
                next(csv_reader)  # This code skips the title so it doesn't print it into the file we opened
                for line in csv_reader:
                    # Check if column 2 (AS value) is not empty before appending the data
                    if line[5].strip():  # Strip whitespace to handle any leading/trailing spaces
                        Data.append((line[0], line[5]))  # Appended the data into our List

    for line in Data:
        position, AS_Value = line
        Points = assign_points(position)
        if AS_Value not in Points_Dict:
            Points_Dict[AS_Value] = Points
        else:
            Points_Dict[AS_Value] += Points

    # Sort the Points_Dict in descending order of points
    sorted_points_dict = dict(sorted(Points_Dict.items(), key=lambda item: item[1], reverse=True))

    # Write the sorted data to the CSV file
    with open(Out_File, "w", newline="") as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(['Points', 'Association Name'])  # Names of the columns
        for AS_Value, Points in sorted_points_dict.items():
            csv_writer.writerow([Points, AS_Value])



button = tk.Button(root, text = "2017 WakaNats Results",font=('Arial',18), command=Process_2017)
button.pack(pady=20)

button = tk.Button(root, text = "2018 WakaNats Results",font=('Arial',18), command=Process_2018)
button.pack(pady=20)

root.mainloop()


