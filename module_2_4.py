numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    for j in range(1, numbers[i]-1):
        if numbers[i] % numbers[j] == 0:
            if numbers[i] not in not_primes:
                not_primes.append(numbers[i])
for i in range(1, len(numbers)):
    if numbers[i] not in not_primes:
        primes.append(numbers[i])
print(f'Простые числа: {primes}')
print(f'Непростые числа: {not_primes}')
