# Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not
a=input('Enter a city name: ')
with open('cities.txt','r') as f:
    if a in f.read():
        print(a,'is in cities.txt File')
    else:
        print(a,'not in cities.txt File')
