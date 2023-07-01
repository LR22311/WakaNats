import os
import csv


def scoring():
    My_dir = r"C:\Users\lr817\OneDrive\Desktop\WakaNats\WakaNats2017\003-Heat 1-03.csv"

    with open(My_dir) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the first row (header)

        points = []
        for row in csv_reader:
            position = int(row[0])  # Extract the position from the first column
            if position == 1:
                points.append(8)
            elif position == 2:
                points.append(7)
            elif position == 3:
                points.append(6)
            elif position == 4:
                points.append(5)
            elif position == 5:
                points.append(4)
            elif position == 6:
                points.append(3)
            elif position == 7:
                points.append(2)
            elif position <= 8:
                points.append(1)
            else:
                points.append(0)

        print(points)

scoring()
    
