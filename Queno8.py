# Write a Python script to create a copy of a file.
def cp_file(filename1,filename2):
    with open(filename1,'r') as f:
        file1=f.read()
        file1=file1.rstrip('\n')
        with open(filename2,'w') as f2:
            f2.write(file1)
a=input('Enter file name which file you want to copy: ')
b=input('enter in which file you want to past the data: ')
cp_file(a,b)