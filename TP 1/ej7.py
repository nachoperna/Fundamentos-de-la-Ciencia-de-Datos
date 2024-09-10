# Escribir un programa que genere una lista de los primeros 20 números de la secuencia de Fibonacci.

fib = [1,1]


def show(fib):
    print("Secuencia: ")
    for i in fib:
        print(f"{i}")

def fibonacci(fib):
    n = len(fib)
    while (n < 20):
        fib.append(fib[n-1] + fib[n-2])
        n += 1
    show(fib)

fibonacci(fib)