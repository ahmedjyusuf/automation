import os

count = 0
#folder containing the files
os.chdir(f'/Users/ahmedyusuf/Test/') 
for f in os.listdir():
    
    # the if statement is for text files only. if you need to rename all files in the directory
    # remove the if statement or specify the file type you want to rename
    
    if f.endswith(".txt"):
        count += 1
        file_number = str(count).zfill(2)
        extension = os.path.splitext(f)[-1]
        new_name = f'{file_number}{extension}'
        os.rename(f, new_name)
        
        print(f'The old name was\n{f}\nthe new name is\n{new_name}\n')
