def calculate(order, x, y):
    if order == "add":
        return x + y
    elif order == "subtract":
        return x - y
    elif order == "multiply":
        return x * y
    elif order == "divide":
        return x % y

        print (calculate(add, 2, 2))