# 1 — Fibonacci Usando Função Recursiva

def fib1(n: int) -> int:
    if n < 2:
        return n  # caso base
    else:
        return fib1(n - 2) + fib1(n - 1)  # função recursiva


if __name__ == "__main__":
    print(fib1(10))
