#
##7.	Given a string, str1=""”Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""
##a.	Build a dictionary, with "words as key" --> Frequency of occurrence as value
#E.g. Python 7, is3
#b.	Print the top 5 words with their frequency of occurrence



str01= "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."
def func(abc):
    d1={}
    a=abc.split()
    #print(a)
    a.sort()
    #print(a)
    #print("********************************************************")
    i=0
    list1=[]
    while(i<len(a)):
       for j in range(i,len(a)):
            if a[i] in list1:
                break
            list1.append(a[i])
        
       i+=1
    #print(list1)
    for i in range(0,len(list1)):
        #d1.add(list1[i],a.count(i))
        d1[list1[i]]=a.count(list1[i])
    print(d1)


    print("The top 5 most occuring words are : ",(sorted(d1.items(), key=lambda kv:kv[1], reverse=True)[:5]))



func(str01)