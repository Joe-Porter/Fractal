import turtle
import time

t = turtle.Pen()

D = 0
d = 0

print("The equation is T = 0 + (n-1)d")
D = int(input("\nPick a number between 0 and 50: "))

if D <= 50 and D >= 10:

    while d <= 500:
        d = d + D
        t.forward(d)
        t.right(90)
else:
    print("Invalid Input")

time.sleep(5)