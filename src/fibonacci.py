def fibonacci(n):
    fib_series = [1, 1]
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series


n = int(input("Digite o valor de N para gerar a série de Fibonacci até o N-ésimo termo: "))

fibonacci_series = fibonacci(n)
print("Série de Fibonacci até o", n, "ésimo termo:", fibonacci_series)