import numpy as np

_h = 1
_alpha = 2


def f(x: list) -> float:
    return x[0] ** 3 + x[1] ** 3 - 3 * x[0] * x[1]


# def f(x: list) -> float:
#     return (x[0] - x[1]) ** 2 + (x[0] ** 2 - x[1] + 2) ** 2


def norm(x: list) -> float:
    return np.sqrt(x[0] ** 2 + x[1] ** 2)


def seach(x, h):
    return [
        [x[0] + h, x[1]],
        [x[0] - h, x[1]],
        [x[0], x[1] + h],
        [x[0], x[1] - h]
    ]


n = 2  # пространство
lenght = 1  # длина ребра симлекса
alpha = .5  # коэфф. сжатия
eps = 1e-4  # точность
__x = [1.5, .7]
h = [.5, .5]
machineAcc = 0.000000001

for _ in range(100):
    value = f(__x)
    search_x = seach(__x, _h)

    for i in search_x:
        if f(i) < value:
            x_base = i
            x_0 = [[_h * x_base[0] - search_x[2][0]], [_h * x_base[1] - search_x[1][1]]]

    if norm([_h, _h]) < eps:
        answer = x_0
        break

    _h //= _alpha

# Симплексный метод
p = lenght * ((n + 1) ** .5 + n - 1) / (n * 2 ** .5)
g = p - lenght * (2 ** .5 / 2)


def vertex_simplex(x):
    V_simplex = []

    for i in range(n):
        temp = []
        for j in range(n):
            if i == j:
                temp += [p]
            else:
                temp += [g]

        V_simplex += [temp]

    return [x] + V_simplex


def geo_middle_simplex(V_simplex):
    x = []
    for i in np.transpose(V_simplex):
        x += [(1 / (n + 1)) * sum(i)]
    return x


def value_F_vertex(V_simplex):
    F = []
    for row in V_simplex:
        F += [f(row)]
    return F


def mirror_vertex(V_simplex, vertex=None):
    new_V = []
    for row in np.transpose(V_simplex):
        summ = 0
        for i in range(len(row)):
            if i != vertex:
                summ += row[i]
        new_V += [(2 / n) * summ]

    return np.array(new_V) - np.array(V_simplex[vertex])


def new_simplex(V_simplex, vertex):
    V = []
    for i in range(len(V_simplex)):
        temp = []
        for j in range(len(V_simplex[i])):
            temp += [lenght * V_simplex[i][j] + (1 - lenght) * V_simplex[vertex][j]]

        V += [temp]
    return V


# print(f'{p = }\n{g = }\n\n')

V_simplex = vertex_simplex(__x)

for i in range(500):
    _x = geo_middle_simplex(V_simplex)
    # print(f'{V_simplex = }')
    # print(f'{_x = }\n\n')

    F = value_F_vertex(V_simplex)
    # print(f'{F = }\n\n')

    temp_F = max(F)
    vertex = F.index(temp_F)

    mirror_V_simplex = mirror_vertex(V_simplex, vertex)
    value = f(mirror_V_simplex)
    if value > temp_F:
        lenght *= alpha
        temp_F = min(F)
        vertex = F.index(temp_F)
        # print(f'{lenght = }\n\n')

        V_simplex = new_simplex(V_simplex, vertex)
        new_x = geo_middle_simplex(V_simplex)
        # print(f'{V_simplex = }\n\n')
        # print(f'f(V) = {value} > F = {temp_F}\n\n{V_simplex = }\n\n{new_x = }\n\n')

    else:
        V_simplex[vertex] = list(mirror_V_simplex)
        new_x = geo_middle_simplex(V_simplex)
        # print(f'f(V) = {value} < F = {temp_F}\n\n{V_simplex = }\n\n{new_x = }\n\n')

    _norm = norm([new_x[0] - _x[0], new_x[1] - _x[1]])
    _abs = abs(f(new_x) - f(_x))
    # print(f'|| new_x - x || = {_norm}\n|f(new_x) - f(x)| = {_abs}\n\n')

    if _norm < eps and _abs < eps:
        print(new_x)
        break

    # print('-' * 100)


def utilSearch(b, h, f):
    bres = b[:]
    fb = f(bres)
    for i in range(0, len(bres)):
        bn = bres
        bn[i] = bn[i] + h[i]
        fc = f(bn)
        if fc + machineAcc < fb:
            bres = bn
            fb = fc
        else:
            bn[i] = bn[i] - 2 * h[i]
            fc = f(bn)
            if fc + machineAcc < fb:
                bres = bn
                fb = fc
    return bres


# Метод Хука-Дживса
def HJ(b1, h, e, f):
    z = 0.1
    runOuterLoop = True
    while (runOuterLoop):
        runOuterLoop = False
        runInnerLoop = True
        xk = b1  # step1
        b2 = utilSearch(b1, h, f)  # step2
        while runInnerLoop:
            runInnerLoop = False
            for i in range(len(b1)):  # step3
                xk[i] = b1[i] + 2 * (b2[i] - b1[i])
            x = utilSearch(xk, h, f)  # step4
            b1 = b2  # step5
            fx = f(x)
            fb1 = f(b1)
            if fx + machineAcc < fb1:  # step6
                b2 = x
                runInnerLoop = True  # to step3
            elif fx - machineAcc > fb1:  # step7
                runOuterLoop = True  # to step1
                break
            else:
                s = 0
                for i in range(len(h)):
                    s += h[i] * h[i]
                if e * e + machineAcc > s:  # step8
                    break  # to step10
                else:
                    for i in range(len(h)):  # step9
                        h[i] = h[i] * z
                    runOuterLoop = True  # to step1
    return b1  # step10


print(HJ(__x, h, eps, f))
