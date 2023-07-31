import os
import csv
import tkinter as tk
from collections import defaultdict

root = tk.Tk()
root.geometry("500x500")
root.title("WakaNate")

def assign_points(position):
    if position == '':
        return 0
    position = int(position)
    if position == 1:
        return 8
    elif position == 2:
        return 7
    elif position == 3:
        return 6
    elif position == 4:
        return 5
    elif position == 5:
        return 4
    elif position == 6:
        return 3
    elif position == 7:
        return 2
    else:
        return 1

def process_data(year):
    keyword = 'Final'
    my_dir = rf'lif Files for WakaNats\WakaNats{year}'
    out_file = rf'Final Results\FinalResultsOf{year}.csv'
    data = []
    points_dict = defaultdict(int)

    for root, _, files in os.walk(my_dir):
        final_keyword_files = (file for file in files if keyword in file)
        for final_name in final_keyword_files:
            final_file_path = os.path.join(root, final_name)
            with open(final_file_path, 'r') as og_data:
                csv_reader = csv.reader(og_data)
                next(csv_reader)
                for line in csv_reader:
                    if not line[0]:
                        continue
                    data.append((line[0], line[5]))
    for position, as_value in data:
        points = assign_points(position)
        points_dict[as_value] += points

    sorted_points = dict(sorted(points_dict.items(), key=lambda item: item[1], reverse=True))

    with open(out_file, "w", newline="") as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(['Points', 'Association Name'])  # Corrected typo here
        for as_value, points in sorted_points.items():
            csv_writer.writerow([points, as_value])

    os.startfile(out_file)

def process_2017():
    process_data(2017)

def process_2018():
    process_data(2018)

button_2017 = tk.Button(root, text="2017 WakaNats Results", font=('Arial', 18), command=process_2017)
button_2017.pack(pady=20)

button_2018 = tk.Button(root, text="2018 WakaNats Results", font=('Arial', 18), command=process_2018)
button_2018.pack(pady=20)

root.mainloop()


            
            

    

    














