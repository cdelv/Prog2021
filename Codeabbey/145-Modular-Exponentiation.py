def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        # If exponent is odd, multiply base with result and take modulo
        if exponent % 2 == 1:
            result = (result * base) % modulus
        # Square the base and take modulo
        base = (base * base) % modulus
        exponent //= 2
    return result


Answer = []
for _ in range(int(input())):
    A, B, M = map(int, input().split())
    Answer.append(modular_exponentiation(A, B, M))

print(' '.join(map(str, Answer)))