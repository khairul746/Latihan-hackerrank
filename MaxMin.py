def maxMin(k, arr):
    arr = sorted(arr)
    unfairness = [] 
    for i in range(len(arr)-k+1):
        arrk = arr[i],arr[i+k] 
        unfairness.append(max(arrk)-min(arrk)) 
    return min(unfairness)