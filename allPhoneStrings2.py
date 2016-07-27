def allPhoneStrings2(myMap, num):
    stringList = []
    currList = []
    for i in xrange(len(num)):
        options = myMap[num[i]]
        if stringList:
            for x in options:
                for prefix in stringList:
                    currList.append(prefix + x)
            stringList = currList
            currList = []
        else:
            stringList = options

    return stringList

testMap = {"1":['a','b'], "2":['c','d']}
print(allPhoneStrings2(testMap, "1"))
print "\n\n"
print(allPhoneStrings2(testMap, "12"))
print "\n\n"
print(allPhoneStrings2(testMap, "222"))
