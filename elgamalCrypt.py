import random

def mod_exp(base, exponent, mod):
    """
    Быстрое возведение в степень по модулю.

    Эта функция вычисляет (base^exponent) mod mod эффективно,
    используя метод "возведения в степень через двоичное разложение".

    Идея:
    - Если степень нечётная, умножаем результат на текущий base.
    - Каждый шаг возводим base в квадрат по модулю.
    - Делим степень на 2 (целочисленно), пока она не станет 0.
    """
    result = 1
    base = base % mod  # берем остаток от base, чтобы уменьшить числа
    while exponent > 0:
        if exponent % 2 == 1:  # если степень нечётная
            result = (result * base) % mod
        base = (base * base) % mod
        exponent = exponent // 2
    return result

def elgamal_keygen(p, g):
    """
    Генерация ключей для криптосистемы Эль-Гамаля.

    - p — простое число (модуль),
    - g — генератор группы по модулю p,
    - x — секретный ключ (случайное число),
    - y = g^x mod p — открытый ключ.

    Возвращает пару: (публичный ключ (p, g, y), приватный ключ x).
    """
    x = random.randint(2, p-2)       # секретный ключ (выбирается случайно)
    y = mod_exp(g, x, p)             # открытый ключ
    return (p, g, y), x

def elgamal_encrypt(m, public_key):
    """
    Шифрование сообщения m с помощью публичного ключа.

    - m — число (сообщение),
    - public_key = (p, g, y).

    Возвращает пару (a, b) — шифротекст.
    """
    p, g, y = public_key
    k = random.randint(2, p-2)       # случайное число для шифрования
    a = mod_exp(g, k, p)
    b = (m * mod_exp(y, k, p)) % p
    return (a, b)

def elgamal_decrypt(cipher, private_key, p):
    """
    Расшифровка шифротекста cipher = (a, b) приватным ключом.

    - private_key — секретный ключ x,
    - p — модуль.

    Расшифровка: m = b * a^{-x} mod p
    """
    a, b = cipher
    s = mod_exp(a, private_key, p)          # s = a^x mod p
    s_inv = pow(s, -1, p)                   # обратный элемент к s по модулю p
    return (b * s_inv) % p

# Пример:
p = 467       # простое число
g = 2         # генератор
message = 123 # сообщение (число)

public, private = elgamal_keygen(p, g)
cipher = elgamal_encrypt(message, public)
decrypted = elgamal_decrypt(cipher, private, p)

print("Публичный ключ:", public)
print("Шифр:", cipher)
print("Дешифр:", decrypted)  # должно совпасть с исходным message

# Дополнительные примеры:
message2 = 200
cipher2 = elgamal_encrypt(message2, public)
print("Шифр для 200:", cipher2)
print("Дешифровка:", elgamal_decrypt(cipher2, private, p))

message3 = 1
cipher3 = elgamal_encrypt(message3, public)
print("Шифр для 1:", cipher3)
print("Дешифровка:", elgamal_decrypt(cipher3, private, p))

input()  # Чтобы программа не закрылась сразу
