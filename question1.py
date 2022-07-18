def range1(num):
    lastNum = 0
    for i in range(num):
        sum = lastNum + i
        print("Current Number:", i, "Previous Number: ", lastNum," Sum: ", sum)
        previousNum = i

print("The output is: ")
range1(10)