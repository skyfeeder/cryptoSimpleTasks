def mod_inverse(a, n):
    """
    Ищет обратный элемент к числу a по модулю n, если он существует.

    Обратный элемент x — это число, при умножении с a по модулю n даёт 1:
    (a * x) % n == 1

    Если такого элемента нет (a и n не взаимно простые), функция выдаст ошибку.

    Используется расширенный алгоритм Евклида (extended_gcd),
    который находит НОД и коэффициенты уравнения Безу: a*x + n*y = gcd(a,n).
    """
    g, x, _ = extended_gcd(a, n)
    if g != 1:
        raise ValueError(f"Обратного элемента не существует для {a} по модулю {n}")
    return x % n

def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида (рекурсивный).

    Возвращает кортеж (g, x, y), где:
    - g = НОД(a, b) — наибольший общий делитель,
    - x, y — такие числа, что a*x + b*y = g.

    Это основа для поиска обратного элемента по модулю.
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def affine_encrypt(text, a, b):
    """
    Афинное шифрование текста.

    Формула шифрования для каждой буквы x (число от 0 до 25):
    E(x) = (a*x + b) mod 26

    text — входной текст (будет преобразован в верхний регистр),
    a, b — ключи шифрования.

    Возвращает зашифрованный текст.
    """
    result = ''
    for ch in text.upper():
        if ch.isalpha():  # если буква
            x = ord(ch) - ord('A')  # преобразуем букву в число 0..25
            result += chr(((a * x + b) % 26) + ord('A'))  # шифруем и обратно в букву
        else:
            result += ch  # прочие символы остаются без изменений
    return result

def affine_decrypt(cipher, a, b):
    """
    Афинная расшифровка текста.

    Для расшифровки используется обратный элемент a_inv по модулю 26,
    и формула:
    D(y) = a_inv * (y - b) mod 26

    cipher — зашифрованный текст,
    a, b — ключи шифрования (те же, что и для шифровки).

    Возвращает исходный текст.
    """
    a_inv = mod_inverse(a, 26)  # обратный элемент к a по модулю 26
    result = ''
    for ch in cipher:
        if ch.isalpha():
            y = ord(ch) - ord('A')
            result += chr(((a_inv * (y - b)) % 26) + ord('A'))
        else:
            result += ch
    return result


# Пример:
text = "HELLOSIMANCHEV"
a, b = 5, 8

cipher = affine_encrypt(text, a, b)
print("Исходный текст:", text)
print("Зашифрованный текст:", cipher)

decrypted = affine_decrypt(cipher, a, b)
print("Расшифровка:", decrypted)

# Дополнительные примеры:

text2 = "CRYPTOGRAPHY"
cipher2 = affine_encrypt(text2, a, b)
print("\nИсходный текст:", text2)
print("Зашифрованный текст:", cipher2)
print("Расшифровка:", affine_decrypt(cipher2, a, b))

text3 = "AFFINECIPHER123"
cipher3 = affine_encrypt(text3, a, b)
print("\nИсходный текст:", text3)
print("Зашифрованный текст:", cipher3)
print("Расшифровка:", affine_decrypt(cipher3, a, b))

input()  # Чтобы программа не закрылась сразу
