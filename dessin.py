import turtle # module pour le dessin

def cercle(r_min: int, r_max: int, pas: int):
    """
    cercle(your_minimum_value, your_maximum_value, the_increment)
    """
    for r_max in range(r_max):
        turtle.circle(r_min)
        r_min += pas

a = int(input("entre ta valeur min : "))
b = int(input("entre ta valeur max : "))
c = int(input("entre ton pas : "))
cercle(a, b, c)