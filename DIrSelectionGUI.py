import os,csv
import tkinter as tk

root= tk.Tk()

root.geometry("500x500")
root.title("WakaNats")




def Process_2018():
    keyword= 'Final'
    My_Dir = r'lif Files for WakaNats\WakaNats2018'
    Out_File = 'Final Results\FinalResultsOf2018.csv'

    unordered_data = [] #List to store column 1 and 2s data

    for root, sub_dirs, files in os.walk(My_Dir):
            Final_Files = (file for file in files if keyword in file)
            for file_name in Final_Files:
                New_Path = os.path.join(root, file_name)#This part finds the files with the keyword "Final"
                with open(New_Path,'r') as Raw_Results:
                    csv_reader = csv.reader(Raw_Results)
                    next(csv_reader) #This code skips the title so it doesnt print it into the file we opened
                    for line in csv_reader:
                        unordered_data.append((line[0],line[5]))#appended the data into our List

    sorted_data = sorted(unordered_data, key=lambda x: x[1]) #Sort the data by column 6 in alphabetical order
                        



    with open(Out_File, "w", newline="") as output_csv:
        csv_writer = csv.writer(output_csv)#This part is used to open up the file where we will write the data needed for the assesment
        csv_writer.writerow(['Pos','AS'])#Names of the columns
        for line in sorted_data:
            csv_writer.writerow(line)#Writing the data


def Process_2017():
    keyword= 'Final'
    My_Dir = r'lif Files for WakaNats\WakaNats2017'
    Out_File = 'Final Results\FinalResultsOf2017.csv'

    unordered_data = [] #List to store column 1 and 2s data

    for root, sub_dirs, files in os.walk(My_Dir):
            Final_Files = (file for file in files if keyword in file)
            for file_name in Final_Files:
                New_Path = os.path.join(root, file_name)#This part finds the files with the keyword "Final"
                with open(New_Path,'r') as Raw_Results:
                    csv_reader = csv.reader(Raw_Results)
                    next(csv_reader) #This code skips the title so it doesnt print it into the file we opened
                    for line in csv_reader:
                        unordered_data.append((line[0],line[5]))#appended the data into our List

    sorted_data = sorted(unordered_data, key=lambda x: x[1]) #Sort the data by column 6 in alphabetical order
                        



    with open(Out_File, "w", newline="") as output_csv:
        csv_writer = csv.writer(output_csv)#This part is used to open up the file where we will write the data needed for the assesment
        csv_writer.writerow(['Pos','AS'])#Names of the columns
        for line in sorted_data:
            csv_writer.writerow(line)#Writing the data




button = tk.Button(root, text = "2017 WakaNats Results",font=('Arial',18), command=Process_2017)
button.pack(pady=20)

button = tk.Button(root, text = "2018 WakaNats Results",font=('Arial',18), command=Process_2018)
button.pack(pady=20)

root.mainloop()


