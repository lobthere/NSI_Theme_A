import turtle # module pour le dessin

a = 1
while True:
    if a <= 10:
        turtle.pencolor("blue")
        turtle.circle(a)
        a += 1
    elif a == 20:
        break
    else:
        turtle.pencolor("red")
        turtle.circle(a)
        a += 1
