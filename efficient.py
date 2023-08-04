import os
import csv
import tkinter as tk
from tkinter import *
from collections import defaultdict

root = tk.Tk()#Created a Window
root.geometry("500x500")#Gave the window a size
root.title("WakaNate")#Named the window

def assign_points(position):#The points system
    if position == '':
        return 0
    position = int(position)
    if position == 1:#If the position is 1 points = 8
        return 8
    elif position == 2:#If the position is 2 points = 7
        return 7
    elif position == 3:#If the position is 3 points = 6
        return 6
    elif position == 4:#If the position is 4 points = 5
        return 5
    elif position == 5:#If the position is 5 points = 4
        return 4
    elif position == 6:#If the position is 6 points = 3
        return 3
    elif position == 7:#If the position is 7 points = 2
        return 2
    else:
        return 1#if the position is anything other then the numbers above points = 1

def process_data(year):#function which process the data
    keyword = 'Final'#keyword to search for in folder
    my_dir = rf'lif Files for WakaNats\WakaNats{year}'#the directory where the data is stored, this should be named as shown here as if it isnt itll not work
    out_file = rf'Final Results\FinalResultsOf{year}.csv'#the directory where the new organized data will be stored
    data = []#list of where the orignal data is temporarly stored for use
    points_dict = defaultdict(int)#gives points_dict to ability to remove duplicates and assign points to each association name according te assign_points
    found_files = []#stores all the files that are processed
    list_of_files.delete(0,END)#clears the list box

    for root, _, files in os.walk(my_dir):
        final_keyword_files = (file for file in files if keyword in file) #looks for the keyword in all the files and stores it in one variable
        for final_name in final_keyword_files:
            final_file_path = os.path.join(root, final_name)#joins the root and the final name path together
            with open(final_file_path, 'r') as og_data:#reads all the data that was found due to the keyword
                csv_reader = csv.reader(og_data)#make a readinf variable
                next(csv_reader)#skips the title for each csv file
                for line in csv_reader:
                    if not line[0]:#if a element has a empty string, it gets skiped
                        continue
                    data.append((line[0], line[5]))#all the data that was found in the csv files are stored in one list
                    found_files.append(final_name)#
    for position, as_value in data:
        points = assign_points(position)
        points_dict[as_value] += points

    sorted_points = dict(sorted(points_dict.items(), key=lambda item: item[1], reverse=True))

    with open(out_file, "w", newline="") as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(['Points', 'Association Name'])  # Corrected typo here
        for as_value, points in sorted_points.items():
            csv_writer.writerow([points, as_value])        
    for item in found_files:
        list_of_files.insert(END, item)
    os.startfile(out_file)

def process_2017():
    process_data(2017)

def process_2018():
    process_data(2018)

button_2017 = tk.Button(root, text="2017 WakaNats Results", font=('Arial', 18), command=process_2017)
button_2017.pack(pady=20)

button_2018 = tk.Button(root, text="2018 WakaNats Results", font=('Arial', 18), command=process_2018)
button_2018.pack(pady=20)

label = tk.Label(root,text="Files being processed", font =('Arial',11))
label.pack(pady=5)

list_of_files = tk.Listbox(root)
list_of_files.pack(pady = 5)

root.mainloop()


            
            

    

    














