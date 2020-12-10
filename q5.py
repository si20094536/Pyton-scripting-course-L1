#5.	Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
#i.	 [1, 2, 2, 3], [2, 2, 3, 3, 3]

l1= [1, 2, 2, 3]
l2= [2, 2, 3, 3, 3]

#def func(abc):
#    set11=set(abc)
#    print("The original list=: ",abc)
#    print("The list without duplicates=: ",list(set11))
#func(l1)
#func(l2)



#   OR



def func(abc):
    print("The original list=: ",abc)
    i=0
    list1=[]
    abc.sort()
    while(i<len(abc)):
       for j in range(i,len(abc)):
            if abc[i] in list1:
                break
            list1.append(abc[i])
        
       i+=1
    print("The new list without any repitions are: ",list1)
func(l1)
func(l2)





