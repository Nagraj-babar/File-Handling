# Write a Python script to extract book data from a bookfile using pickle. Also print extracted book data.
import pickle
file='bookfile.pkl'
with open(file,'rb') as f:
    file_data=pickle.load(f)
    print(file_data)
    for data in file_data:
        print(data,'=',file_data[data])