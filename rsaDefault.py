def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида.

    Что делает:
    - Находит НОД (наибольший общий делитель) чисел a и b.
    - Возвращает троицу (g, x, y), где g — НОД(a, b), 
      и такие числа x, y, что выполняется уравнение: a*x + b*y = g.

    Особенности:
    - Реализован рекурсивно.
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def mod_inverse(a, n):
    """
    Находит обратный элемент к a по модулю n (если существует).

    Обратный элемент x — такой, что (a * x) % n = 1.

    Использует расширенный алгоритм Евклида для нахождения x.

    Если обратного элемента не существует (когда a и n не взаимно просты), 
    функция выбрасывает ошибку.
    """
    g, x, _ = extended_gcd(a, n)
    if g != 1:
        raise ValueError(f"Обратного элемента не существует для {a} по модулю {n}")
    return x % n


def rsa_keygen(p, q, e):
    """
    Генерация пары ключей RSA.

    - p, q — простые числа (секретные).
    - e — открытая экспонента (обычно небольшое простое число, взаимно простое с phi).
    Возвращает:
    - public_key = (e, n)
    - private_key = (d, n), где d — обратный к e по модулю phi.

    phi = (p-1)*(q-1)
    d * e ≡ 1 (mod phi)
    """
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)


def rsa_encrypt(msg, public_key):
    """
    Шифрование сообщения msg с помощью открытого ключа public_key.

    msg — целое число, меньше n.
    Возвращает зашифрованное число (шифртекст).
    """
    e, n = public_key
    return pow(msg, e, n)


def rsa_decrypt(cipher, private_key):
    """
    Расшифровка cipher с помощью приватного ключа private_key.

    Возвращает исходное сообщение.
    """
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

input()  # Чтобы программа не закрывалась сразу
