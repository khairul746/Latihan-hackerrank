def birthday(s:int, d:int, m:int):
    """birthday has the following parameter(s):
    s[n]: the numbers on each of the squares of chocolate
    d   : Ron's birth day
    m   : Ron's birth month
    """
    chunks = [s[i:i+m] for i in range(0, len(s))]
    count = 0
    for chunk in chunks:
        if sum(chunk) == d :
            count += 1
    return count
s = [1,2,3,1,2]
print(birthday(s,4,2))
