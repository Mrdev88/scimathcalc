import typer
import numpy as np
from mathparse import mathparse
import re

app = typer.Typer()

@app.command()
def shell():
    startshell()


@app.command()
def add(add_x: int, add_y: int):
    add_result = add_x + add_y
    print(f"{add_x} + {add_y} = {add_result}")

@app.command()
def subtract(subtract_x: int, subtract_y: int):
   subtract_result = subtract_x - subtract_y
   print(f"{subtract_x} - {subtract_y} = {subtract_result}")

@app.command()
def multiply(multiply_x: int, multiply_y: int):
    multiply_result = multiply_x * multiply_y
    print(f"{multiply_x} * {multiply_y} = {multiply_result}")

@app.command()
def divide(divide_x: int, divide_y: int):
    if divide_y == 0:
        print("Error: Division by zero is not allowed.")
    else:
        divide_result = divide_x / divide_y
        print(f"{divide_x} / {divide_y} = {divide_result}")

@app.command()
def exp(base: int, exponent: int):
    exp_result = base ** exponent
    print(f"{base} ^ {exponent} = {exp_result}")

@app.command()
def sqrt(sqrt_number: int):
    sqrt_result = np.sqrt(sqrt_number)
    print(f"√({sqrt_number}) = {sqrt_result}")

@app.command()
def greater(gt_x :int, gt_y: int):
    if gt_x > gt_y:
        print(f"{gt_x} is greater than {gt_y}")

@app.command()
def pi():
    pi = np.pi
    print(pi)
   
def startshell():
    print("Scimathcalc Shell")
    print("Type 'exit' to exit the shell.")
    while True:
        user_input = input("Scimathcalc>")
        if user_input.lower() == "exit":
            break
        spaced_input = re.sub(r'([+\-*/^()])', r' \1 ', user_input)
        print(mathparse.parse(spaced_input))

if __name__ == "__main__":
    app()
