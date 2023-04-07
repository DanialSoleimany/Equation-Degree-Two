a = int(input("a:\n"))
b = int(input("b:\n"))
c = int(input("c:\n"))

# (a * x ** 2) + (b * x) + c = 0

delta = (b ** 2) - (4 * a * c)

if a != 0:
    if delta >= 0:
        x1 = ((-1*b) + (delta ** .5)) / (2 * a)
        x2 = ((-1*b) - (delta ** .5)) / (2 * a)
        print("x1 = {0:.2f}\nx2 = {1:.2f}".format(x1, x2))
    else:
        print("No roots")
else:
    print("Equation is not degree 2")