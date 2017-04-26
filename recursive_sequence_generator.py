def sequence(number, seq):
    if number == 1:
        return seq
    elem = number / 2 if number % 2 == 0 else (3*number) + 1
    seq.append(elem)
    return sequence(elem, seq)


longest_chain = []

for i in range(1, 1000000):
    chain = sequence(i, [])
    if len(chain) > len(longest_chain):
        longest_chain = chain
        print(i)

print(len(longest_chain))