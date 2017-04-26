value = 600851475143
for i in range(2, (600851475143+1)//2):
    while value % i == 0:
        value /= i
    if value == 1:
        print(i)
        break
