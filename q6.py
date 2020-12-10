##6.	Write a function to print the information in the dictionary(bookstore) in the given format

##bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}


##BOOKSTORE

##'Learning XML', 'Erik T. Ray', '2003', '39.95' 
##'Everyday Italian', 'Giada De Laurent is', '2005', '30.00']
 ##'Harry Potter', 'J K. Rowling', '2005', '29.99']


#d1={}
d1={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
def func(abc):
    print("BOOKSTORE")
    bookstore=list(abc["New Arrivals"].keys())
    print(bookstore)
    bookstore.sort(key=lambda x : len(x) )
    print(bookstore)
    for i in range(0,len(bookstore)):
        print(abc["New Arrivals"][bookstore[i]])
func(d1)