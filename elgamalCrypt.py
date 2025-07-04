import random

def mod_exp(base, exponent, mod):
    """Быстрое возведение в степень по модулю"""
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:  # если степень нечётная
            result = (result * base) % mod
        base = (base * base) % mod
        exponent = exponent // 2
    return result

def elgamal_keygen(p, g):
    """Генерация ключей"""
    x = random.randint(2, p-2)       # секретный ключ
    y = mod_exp(g, x, p)             # открытый ключ
    return (p, g, y), x

def elgamal_encrypt(m, public_key):
    """Шифрование"""
    p, g, y = public_key
    k = random.randint(2, p-2)
    a = mod_exp(g, k, p)
    b = (m * mod_exp(y, k, p)) % p
    return (a, b)

def elgamal_decrypt(cipher, private_key, p):
    """Дешифрование"""
    a, b = cipher
    s = mod_exp(a, private_key, p)
    s_inv = pow(s, -1, p)  # обратное по модулю
    return (b * s_inv) % p

# Пример
p = 467
g = 2
message = 123

public, private = elgamal_keygen(p, g)
cipher = elgamal_encrypt(message, public)
decrypted = elgamal_decrypt(cipher, private, p)

print("Публичный ключ:", public)
print("Шифр:", cipher)
print("Дешифр:", decrypted)
input() # Для того, чтобы программа не закрывалась сразу