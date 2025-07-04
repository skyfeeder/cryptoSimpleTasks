def extended_gcd(a, b):
    """Расширенный алгоритм Евклида.
    Возвращает (g, x, y), где g — НОД(a, b), и x, y такие, что ax + by = g
    (Реализация с рекурсией)
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inverse(a, n):
    """Ищет обратный элемент к a по модулю n, если он существует"""
    g, x, _ = extended_gcd(a, n)
    if g != 1:
        raise ValueError(f"Обратного элемента не существует для {a} по модулю {n}")
    return x % n

# Пример:
a = 17
n = 125
print(f"Обратный элемент к {a} по модулю {n} — {mod_inverse(a, n)}")
input() # Для того, чтобы программа не закрывалась сразу