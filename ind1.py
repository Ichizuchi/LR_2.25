import math
from multiprocessing import Process

CONST_PRECISION = 1e-07


def func_x(x):
    result = 1 / (math.pow((1 - x), 2))
    return result


def func_y(x):
    result = 1 / math.log10(math.sqrt((1 + x) / (1 - x)))
    return result


def summ_1(x):
    n, s, m, curr = 0, 0, 0, 0
    while True:
        pre = (n + 1) * x ** n
        n += 1
        if abs(curr - pre) < CONST_PRECISION:
            break
        curr = (n + 1) * x ** n
        s += curr
    return s


def summ_2(x):
    n, s, curr = 0, 0, 0
    while True:
        second = 2 * n + 1
        first = x ** (2 * n + 1)
        pre = first / second
        n += 1
        if abs(curr - pre) < CONST_PRECISION:
            break
        curr = first / second
        s += curr
    return s


def compare(first, second, x):
    result = first(x) - second(x)
    print(f"Результат сравнения {result}")


if __name__ == '__main__':
    p1 = Process(target=compare, args=(summ_1, func_x, -0.7))
    p2 = Process(target=compare, args=(summ_2, func_y, 0.35))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
