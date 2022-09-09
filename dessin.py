import turtle # module pour le dessin

def cercle(r_min: int, r_max: int, pas: int):
    for r_max in range(pas):
        turtle.circle(r_min)
        r_min += pas

cercle(5, 50, 5)