import os,csv

keyword= 'Final'
My_Dir = r'CSV files for WakaNats\WakaNats2017'
Out_File = 'FinalResults.csv'

unordereddata = [] #List to store column 1 and 2s data

for root, sub_dirs, files in os.walk(My_Dir):
        FinalFiles = (file for file in files if keyword in file)
        for file_name in FinalFiles:
            NewPath = os.path.join(root, file_name)#This part finds the files with the keyword "Final"
            with open(NewPath,'r') as RawResults:
                csv_reader = csv.reader(RawResults)
                next(csv_reader) #This code skips the title so it doesnt print it into the file we opened
                for line in csv_reader:
                    unordereddata.append((line[0],line[5]))#appended the data into our List

sorted_data = sorted(unordereddata, key=lambda x: x[1]) #Sort the data by column 6 in alphabetical order
                    



with open(Out_File, "w", newline="") as output_csv:
    csv_writer = csv.writer(output_csv)#This part is used to open up the file where we will write the data needed for the assesment
    csv_writer.writerow(['Pos','AS'])#Names of the columns
    for line in sorted_data:
         csv_writer.writerow(line)#Writing the data


