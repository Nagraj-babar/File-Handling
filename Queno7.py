'''Write a Python script to count the number of Python keywords occurring in a python
source file.'''
import keyword
key=keyword.kwlist
with open('E:\Python Programes\Assignement No.2\File Handling\Queno5.py','r') as f:
 list1=f.readlines()
 i=0
 for line in list1:
   line=line.rstrip('\n')
   line1=line.split()
   for line2 in line1:
    for keys in key:
      if keys in line2:
         if len(keys)==len(line2):
          i+=1
      continue
print('Total Keywords in a File is:',i)

     
 
         
    


   
   

