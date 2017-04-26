import functools
import math


def factors(n):
    return set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))

index = 1
triangle_sum = 1
while True:
    if len(factors(triangle_sum)) > 500:
        print(triangle_sum)
        break
    index += 1
    triangle_sum += index