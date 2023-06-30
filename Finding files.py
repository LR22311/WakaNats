import os

keyword = 'final' 
my_dir = 'WakaNats2018'
print('**************Start Print**************')
for root, sub_dirs, files in os.walk(my_dir):
    print('Root Directory Path:', root)
    print('Sub Directories:', sub_dirs)
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'r') as f:
            content = f.read()
            if keyword in content:
                print('Keyword found in file:', file_path)
    print('*' * 25)
print('**********End Print*********')
