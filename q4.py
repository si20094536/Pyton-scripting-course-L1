## 4.	Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple. 
##e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
##      Hint: use a custom key= function to extract the last element form each tuple.
##i.	 [(1, 3), (3, 2), (2, 1)]
##ii.	[(1, 7), (1, 3), (3, 4, 5), (2, 2)]





l1=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
l2= [(1, 3), (3, 2), (2, 1)]
l3= [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
def func(abc):

    print("The list before being sorted is : ",abc)
    abc.sort(key=lambda x: x[1])
    print("The list are being sorted is : ",abc)

func(l1)
func(l2)
func(l3)