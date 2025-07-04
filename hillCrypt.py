import numpy as np # pip install numpy (если запускаешься на декстопе)

def hill_encrypt(text, key_matrix):
    """Шифр Хилла: преобразует каждые 2 буквы с помощью матрицы"""
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    result = ''
    for i in range(0, len(text), 2):
        block = [ord(c) - ord('A') for c in text[i:i+2]]
        encrypted = np.dot(key_matrix, block) % 26
        result += ''.join(chr(num + ord('A')) for num in encrypted)
    return result

# TODO: Обратную матрицу считать сложно, пока только шифрование
key = np.array([[3, 3], [2, 5]])  # Определитель 9 => обратим по mod 26
text = "HIRUSLAN"
print("Шифр Хилла:", hill_encrypt(text, key))
input() # Для того, чтобы программа не закрывалась сразу