n = int(input("Enter Number whose sum needs to be calculated:"))
sum = 0
for number in range(1, n + 1, 1):
    sum = sum + number
print("Sum from 1 to given number is: ",sum)