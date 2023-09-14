import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# №5 f(x) = 2*x**2 + 16/x -> x in [1, 5]

def f(x) -> float:
	return 2*x**2 + 16/x


a = 1
b = 5
eps = 1e-4
n = 10000

figure = plt.subplot()
x = np.linspace(a, b, 100)
# np.arange(a, b, .001)

_x = np.linspace(-0.12, 5, 100)
plt.plot(_x, f(_x))
plt.grid()
plt.show()


counter_iteration_even_search, counter_iteration_golden_ration = \
	n - 2, 0


# Равномерный поиск
minim = f(a + 0*((b - a)/(n + 1))) # начальное минимальное значение функции
point_x_even_search = a + 0*((b - a)/(n + 1)) # начальная точка
for i in range(1, n - 1):

	f_x = f(a + i*((b - a)/(n + 1))) # функция в текущей точки
	if f_x < minim:
		minim = f_x
		point_x_even_search = a + i*((b - a)/(n + 1)) # точка

	# counter_iteration_even_search += 1


# Золотое сечение
y0 = a + ((3 - 5 ** .5) / 2) * (b - a)
z0 = a + b - y0

while True:
	f1 = f(y0)
	f2 = f(z0)

	if f1 <= f2:
		b = z0
		temp = y0
		y0 = a + b - y0
		z0 = temp

	else:
		a = y0
		temp = z0
		y0 = z0
		z0 = a + b - z0

	if abs(a - b) <= eps:
		point_x_golden_ration = (a + b) / 2
		break

	else: counter_iteration_golden_ration += 1


plt.plot(x, f(x), label='График функции 2*x^2 + 16/x')

plt.plot(point_x_even_search, label=f'Равномерный поиск: {point_x_even_search}')
plt.scatter(point_x_even_search, minim, s=100)

# plt.plot(point_x_golden_ration, label=f'Золотое сечение: {point_x_golden_ration}')
# plt.scatter(point_x_golden_ration, f(point_x_golden_ration), s=50)

plt.legend()
plt.grid()
plt.show()


print(f'Кол-во итераций равномерного поиска - {counter_iteration_even_search}')
print(f'Кол-во итераций золотого сечения - {counter_iteration_golden_ration}')