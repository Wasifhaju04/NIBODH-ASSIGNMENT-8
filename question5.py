def areaOfSquare(side):
    return side*side

print("Enter The Side Length of Square: ", end="")
l = float(input())
a = areaOfSquare(l)
print("\nArea = {:.2f}".format(a))