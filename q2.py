## 2.	Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.  

## i.	['axa', 'xyz', 'gg', 'x', 'yyy']
## ii.	['x', 'cd', 'cnc', 'kk']
## iii.	['bab', 'ce', 'cba', 'syanora']

list1=	['axa', 'xyz', 'gg', 'x', 'yyy']
list2=	['x', 'cd', 'cnc', 'kk']
list3=	['bab', 'ce', 'cba', 'syanora']

def func(abc):
    i=0
    count=0
    while(i<len(abc)):
        if(len(abc[i])>1):
            if(abc[i][0]==abc[i][-1]):
                count+=1
        i+=1
    print("The total count of the words is.,:",count)

func(list1)
func(list2)
func(list3)
