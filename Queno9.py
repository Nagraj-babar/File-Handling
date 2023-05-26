'''Write a Python script to store book data in a file. Book data is in the form of a
dictionary in which book name is the key and price is its value. Use pickle to store
data into a file (say bookfile)'''
import pickle
bookdata={'shreebhagavatgeeta':611,'Shivpuran':701,'yajurved':602,'samved':305}
#with open('bookfile.pkl','wb') as f:
    #pickle.dump(bookdata,f)
file3='bookfile.pkl'
with open(file3,'rb') as fi:
        file2=pickle.load(fi)
        print(file2)
    






