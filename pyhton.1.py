print('Icecream')
def division(a, b):
    """Function to divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

x = 10
y = 5
print(f"{x} / {y} = {division(x, y)}")
