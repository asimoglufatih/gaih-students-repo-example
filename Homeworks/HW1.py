list1 = [1,3,5,7,9]
list2 = [0,2,4,6,8]

#merge the list
newList = list1 + list2

listLen = len(newList)

#multiply all values
for i in range(0,listLen):
    newList[i] = newList[i] * 2

#print all types
for i in range(0,listLen):
    print(type(newList[i]))

