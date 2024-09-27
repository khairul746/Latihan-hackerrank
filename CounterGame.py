def counterGame(n):
    bit_count = bin(n).count('1')
    if bit_count % 2 == 0:
        return 'Richard'
    else:
        return 'Louise'
print(counterGame(132))