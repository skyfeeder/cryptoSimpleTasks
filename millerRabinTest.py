import random

def is_prime_mr(n, k=5):
    """Тест Миллера-Рабина с k раундами"""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False

    # Представим n-1 как 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Пример:
print("Является ли 99 простым? Ответ:", is_prime_mr(99))    # False
print("Проверка 561:", is_prime_mr(561))  # False
print("Проверка 101:", is_prime_mr(101))  # True
input() # Для того, чтобы программа не закрывалась сразу