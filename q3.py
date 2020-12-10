## 3.	Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.  
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
##  ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']. 
# Hint: this can be done by making 2 lists and sorting each of them before combining them.
##  i.  	['bbb', 'ccc', 'axx', 'xzz', 'xaa']
##      ii. 	['mix', 'xyz', 'apple', 'xanadu', 'aardvark']


test= ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
list1a= ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
list2b= ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

def func(abc):
    old=abc
    list_new=[]
    abc.sort()
   # print(abc)
    i=0
    while(i<len(abc)):
        if(abc[i][0]=='x' or abc[i][0]=='X'):
            list_new.append(abc[i])
            abc[i]="*"
        i+=1
    i=0
    while(i<len(abc)):
        if(abc[i]!="*"):
            list_new.append(abc[i])
        i+=1
    print("The original list was : ",old)
    print("The ne list after sorting is : ",list_new)

func(test)
func(list1a)
func(list2b)
