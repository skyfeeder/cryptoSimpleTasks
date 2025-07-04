import math

def euler_phi(n):
    """Считает функцию Эйлера φ(n) — количество чисел от 1 до n, взаимно простых с n"""
    result = n
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
    if n > 1:
        result -= result // n
    return result

# Пример:
print(f"φ(125) = {euler_phi(125)}")
input() # Для того, чтобы программа не закрывалась сразу