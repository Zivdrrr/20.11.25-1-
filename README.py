import math
from sympy import symbols, sympify, lambdify

x = symbols('x')

func_str = input("Введіть функцію f(x): ")

try:
    expr = sympify(func_str)
    f = lambdify(x, expr, "math")
except Exception:
    print("Помилка")
    exit()

try:
    x0 = float(input("Введіть перше наближення x0: "))
    x1 = float(input("Введіть друге наближення x1: "))
    eps = float(input("Введіть точність eps: "))
    max_iter = int(input("Введіть максимальну кількість ітерацій: "))
except ValueError:
    print("Помилка")
    exit()

step = 1
while step <= max_iter:
    try:
        fx0 = f(x0)
        fx1 = f(x1)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    except ZeroDivisionError:
        print("Ділення на нуль, метод не працює")
        break

    print(f"Крок {step}: x = {x2:.6f}, f(x) = {f(x2):.6f}")

    if abs(x2 - x1) < eps:  
        print(f"\nНайближчий корінь: x = {x2:.6f}")
        break

    x0, x1 = x1, x2  
    step += 1
else:
    print("Метод не зійшовся за максимальну кількість ітерацій")
