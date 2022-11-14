
# week5 Exercise2

def feetToinches(number1):
    inch = number1 * 12
    print(f"{number1} ft:")
    print(f"... {inch} inches")


    feetTometers(number1)


def feetTometers(number2):
    meter = round(number2 * 0.3048, 4)

    print(f"... {meter} meters")


for A in range(10):
    feetToinches(A)

