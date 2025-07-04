import random
import math

def gcd(a, b):
    """Находит наибольший общий делитель двух чисел"""
    while b:
        a, b = b, a % b
    return a

def is_probable_prime(n, q):
    """
    Проверяет, является ли число n вероятно простым.
    Условия:
    1. a^(n-1) ≡ 1 mod n
    2. gcd(a^((n-1)//q) - 1, n) == 1
    """
    for _ in range(20):  # до 20 попыток найти подходящее a
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            continue  # Условие 1 не выполнено
        t = pow(a, (n - 1) // q, n)
        if gcd(t - 1, n) == 1:
            return True
    return False

def generate_prime(bits=16):
    """
    Генерация вероятно простого числа согласно алгоритму:
    q — начальное простое, n = q*r + 1, проверяется по условиям.
    bits — желаемая длина в битах (по умолчанию 16)
    P.s. Ограничение на биты накладывает следующее ограничение на генерируемое число n: 2^(bits - 1) ≤ n < 2^bits
    """
    q = 3  # Начальное простое число
    while True:
        for _ in range(200):  # Пробуем 200 значений r
            r = random.choice(range(q + (q % 2), 4 * q + 3, 2))  # Чётное r
            n = q * r + 1
            if is_probable_prime(n, q):
                print(f" Найдено вероятно простое n = {n}")
                q = n  # Переходим к следующему шагу
                break
        if q.bit_length() >= bits:
            return q

# Пример:
print(" Генерация простого числа (алгоритм из лекции)...")
prime = generate_prime(bits=16)
print(f"\n Сгенерированное вероятно простое число (16 бит): {prime}")

input() # Для того, чтобы программа не закрывалась сразу
