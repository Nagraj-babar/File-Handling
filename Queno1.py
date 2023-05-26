'''Write a Python script to print the following status of a file:
a. Whether a file is read only
b. Whether a file is closed or not
c. Which file opening mode is used
d. Name of the file'''
a=input('Enter a file name: ')
b=input('Enter file access mode:  ')
try:
 f=open(a,b)
 print('File is open')
 if b=='r':
    print('File is only in read only mode\n','Name of File is a: ',a,'\n','File openning mode: ',b)
 elif b=='w':
    print('File open in write mode\n','Name of File is ',a,'\n','File Opening mode is: ' ,b)
 elif b=='a':
   print('File open in append mode\n','Name of File is ',a,'\n','File opening mode is:',b)
 f.close()
 print('File is close')
except FileNotFoundError:
  print('File not exiest') 