def getTotalX(a, b):
    count = 0
    for i in range(max(a),min(b)+1):
        if all(i % num_a == 0 for num_a in a) and all(num_b % i == 0 for num_b in b):
            count += 1
        else :
            continue
    return count