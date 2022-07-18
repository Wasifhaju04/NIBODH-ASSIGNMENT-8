def quest2(numList):
    firstElement = numList[0]
    lastElement = numList[-1]
    if (firstElement == lastElement):
        return True
    else:
        return False

n = int(input("ENTER THE NUMBER OF LIST: "))
numList = []
for i in range(n):
    element = int(input("ENTER THE ELEMENTS: "))
    numList.append(element)

print("The Result is: ", quest2(numList))

