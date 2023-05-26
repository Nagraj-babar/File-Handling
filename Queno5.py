# Write a Python script to append list of city names in a file ‘cities.txt
def City_names(filename,Text):
    with open(filename,'w') as f:
        for city in Text:
            f.write(city+'\n')
cityname=['Satara','Pune','Mumbai','Nashik','Thane']
City_names('cities.txt',cityname)

    




