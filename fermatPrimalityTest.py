def fermat_primality_test(n, a=2):
    """Проверка простоты числа n по тесту Ферма с основанием a"""
    if pow(a, n - 1, n) == 1:
        return True
    return False

# Пример:
print("Является ли 99 простым? Ответ:", fermat_primality_test(99))    # False
print("Является ли 561 простым? Ответ:", fermat_primality_test(561))  # True - Составное, но является числом Карлмайкла (n : a^(n-1) === 1 (mod n), a - целое и взаимнопростое с n)
print("Является ли 17 простым? Ответ:", fermat_primality_test(17))    # True
input() # Для того, чтобы программа не закрывалась сразу