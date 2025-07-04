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

def affine_encrypt(text, a, b):
    """Афинное шифрование: E(x) = (a * x + b) mod 26"""
    result = ''
    for ch in text.upper():
        if ch.isalpha():
            x = ord(ch) - ord('A')
            result += chr(((a * x + b) % 26) + ord('A'))
        else:
            result += ch
    return result

def affine_decrypt(cipher, a, b):
    """Афинная расшифровка"""
    a_inv = mod_inverse(a, 26)
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
print("Расшифровка:", affine_decrypt(cipher, a, b))
input() # Для того, чтобы программа не закрывалась сразу