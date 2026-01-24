#map(function,iteratable)
# numbers=(23,34,56,3)

# mydata= map(lambda a : a+3 ,numbers)
# print(tuple(mydata))

# myList = [10,20,30,40]

# myData = map( lambda x : x + 2, myList)
# print(list(myData),"mydata")


# myData = list(map(lambda x: x + 2, myList))


# studentsTotal = [350,260,367,480,189]


# myFilteredData = filter(lambda x : x >= 300, studentsTotal)
# print(list(myFilteredData),"myFilteredData")






#lambda
# result = lambda f,e : f*e
# print(result(21,56))

# result = lambda r,w : r/w
# print(result(123,654))

# answer = lambda j,t : j+t
# print(answer(432,78))




#map
# list1 = [3,6,2,57,89]

# mydata = map (lambda d : d+2, list1)
# print(list(mydata))

# tuple1 = [34,21,87,4]

# mydata1 = map(lambda n :n+2,tuple1)
# print(tuple(mydata1))

# list2 = [45,32,23,0]

# mydata2 = map(lambda h : h+3,list2)
# print(list(mydata2))




#filter
# markstotal = [99,89,12,90]

# myfilterdata = filter(lambda v : v>= 80, markstotal)
# print(list(myfilterdata))

# schoolstotal = (789,432,504,57)

# mfd1 = filter(lambda m : m>=203,schoolstotal)
# print(tuple(mfd1))

# fruitstotal = [253,804,291,740]

# mfd2 = filter(lambda j : j>=804,fruitstotal)
# print(list(mfd2))




#reduce
# students = (23,65,85,97,57,121)
# total = reduce(lambda x,y : x + y,  students)
# print(total)