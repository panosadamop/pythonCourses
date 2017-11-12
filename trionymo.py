import math as m

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = b**2-4*a*c

if d > 0:
    x1 = (-b + m.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
    x2 = (-b - m.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
    print("This equation has two solutions: ", x1, " or", x2)
elif d == 0:
    x = (-b+m.sqrt(b**2-4*a*c))/2*a
    print ("This equation has one solutions: "), x
else:
    print("This equation has no real solution")