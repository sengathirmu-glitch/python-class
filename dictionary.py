#intro

md1={
    "fruits":"mango",
    "vegetables":"tomato",
    "diary products":"milk"}

#print(md1)
#print(md1["fruits"])

#no.1 ; get()
#print(md1.get("vegetables"))

#no.2 ; keys()
#print(md1.keys())

#no.3 ; looping
#for i in md1:
#    print(md1[i])

#for a, b in md1.items():
#    print(a, b)

#for a in md1

myDict = {
    "name":"innissai",
    "age":10,
    "mobile":938579435,
    "email":"innisai@gmail.com",
    "name":"sengathir"
}
#keys()
#print(myDict.keys())

#values()
#print(myDict.values())

#items()
#print(myDict.items())

# change the values
#myDict["age"] = 14
#print(myDict,"values - changed")

#myDict.update({"mobile":"1234567890"})
#print(myDict,"updated")

# remove and key-value pairs
#myDict.pop("age")
#print(myDict,"poped data")

# The popitem()
#myDict.popitem()
#print(myDict,"popitem")

# clear
myDict.clear()
print(myDict,"clear")

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
    