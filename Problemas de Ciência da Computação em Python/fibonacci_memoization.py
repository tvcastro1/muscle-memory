# 2 — Fibonacci recursivo usando dicionário para cache e redução da complexidade de tempo,

memo = {0: 0, 1: 1}  # caso base

def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)  # memoization
        # memo[4] = fib2(3) + fib2(2)
        # memo[3] = fib2(2) + fib(1)
        # memo[2] = fib(1) + fib(0) -> o caso base é alcançado.
        # memo[2] = 1 + 0 = 1
    return memo[n]


if __name__ == "__main__":
    print(fib2(4))


