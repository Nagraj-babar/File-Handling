# Write a Python script to create a new file ‘myfile.txt’ and store user entered text.
with open('myfile.txt','a') as f:
    a=input('Enter a text here: ')
    f.write(a)
    

