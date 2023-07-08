import os,csv

keyword= 'Final'
My_Dir = r'CSV files for WakaNats\WakaNats2017'
Out_File = 'FinalResults.csv'

with open(Out_File, "w", newline="") as output_csv:
    csv_writer = csv.writer(output_csv)

    csv_writer.writerow(['Pos','AS'])

    for root, sub_dirs, files in os.walk(My_Dir):
        FinalFiles = (file for file in files if keyword in file)
        for file_name in FinalFiles:
            NewPath = os.path.join(root, file_name)
            with open(NewPath,'r') as RawResults:
                csv_reader = csv.reader(RawResults)
                next(csv_reader)
                for line in csv_reader:
                    csv_writer.writerow([line[0], line[5]])
                    


