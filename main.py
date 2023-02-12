step = float(input("Enter step: "))
desired_approximation = float(input("Enter y val: "))
initial_condition = input("Enter initial condition: ")
xy = initial_condition.split(",")

if len(xy) > 2:
    print("invalid")
    exit()
else:
    current_x = float(xy[0])
    current_y = float(xy[1])


def dydx(x, y):
    return x + y


def eulers_method(dydx, x, y):
    return dydx(x, y) * step + y


while current_x < desired_approximation:
    current_y = eulers_method(dydx, current_x, current_y)
    current_x += step

print("x: " + str(round(current_x, 2)), "\n~y: " + str(current_y))
