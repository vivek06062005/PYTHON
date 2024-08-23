def generate_fibonacci(n):
    fibonacci_list = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list
n = 10
fibonacci_numbers = generate_fibonacci(n)
print(fibonacci_numbers)
