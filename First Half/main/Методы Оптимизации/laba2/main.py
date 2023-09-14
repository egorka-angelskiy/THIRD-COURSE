import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# №5 f(x) = 2*x**2 + 16/x -> x in [1, 5]

def f(x: float) -> float:
	return 2*x**2 + 16/x

def df(x: float) -> float:
	return (4 * x) - 16/(x ** 2)

def ddf(x: float) -> float:
	return 4 + 32/(x ** 3)



x = np.arange(1, 5, 0.01)
plt.plot(x, f(x), label='f(x)')
plt.plot(x, df(x), label='f`(x)')
plt.plot(x, ddf(x), label='f``(x)')
plt.legend()
plt.grid()
plt.show()


# Метод средней точки 
a = 1
b = 5
eps = 1e-4

counter_middle_point = counter_Newton = 0
while True:

	z = (a + b) / 2

	if df(z) > 0: b = z

	else: a = z


	if abs(df(z)) <= eps: 
		middle_point_x = z
		break

	else: counter_middle_point += 1


# Метод Ньютона
a = 1
b = 5

_x = (b - a) / 2
while True:

	_x = _x - (df(_x)/ddf(_x))

	if abs(df(_x)) <= eps:
		Newton_point_x = _x
		break

	else: counter_Newton += 1



plt.plot(x, f(x), label='График функции 2*x^2 + 16/x')

plt.plot(middle_point_x, label=f'Метод средней точки: {middle_point_x}')
plt.scatter(middle_point_x, f(middle_point_x), c='green', s=100)

plt.plot(Newton_point_x, label=f'Метод Ньютона: {Newton_point_x}')
plt.scatter(Newton_point_x, f(Newton_point_x), c='red', s=50)

plt.legend()
plt.grid()
plt.show()

print(f'Кол-во итераций средней точки - {counter_middle_point}')
print(f'Кол-во итераций Ньютона - {counter_Newton}')