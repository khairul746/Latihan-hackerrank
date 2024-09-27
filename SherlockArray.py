def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return 'YES'
        left_sum += value
    return 'NO'
arr = [2,0,0,0]
print(balancedSums(arr))