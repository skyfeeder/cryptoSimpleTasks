def mod_inverse(a, n):
    """Ищет обратный элемент к a по модулю n, если он существует"""
    g, x, _ = extended_gcd(a, n)
    if g != 1:
        raise ValueError(f"Обратного элемента не существует для {a} по модулю {n}")
    return x % n

def extended_gcd(a, b):
    """Расширенный алгоритм Евклида.
    Возвращает (g, x, y), где g — НОД(a, b), и x, y такие, что ax + by = g
    (Реализация с рекурсией)
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1
# 2 функции выше - из алгоритма Евклида

def rsa_keygen(p, q, e):
    """Генерация ключей RSA"""
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def rsa_encrypt(msg, public_key):
    e, n = public_key
    return pow(msg, e, n)

def rsa_decrypt(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)

# Пример:
p, q = 61, 53
e = 17
public, private = rsa_keygen(p, q, e)
message = 42
cipher = rsa_encrypt(message, public)
print("Зашифровано:", cipher)
print("Расшифровано:", rsa_decrypt(cipher, private))
input() # Для того, чтобы программа не закрывалась сразу