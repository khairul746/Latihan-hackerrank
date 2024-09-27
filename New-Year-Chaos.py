def minimumBribes(q):
    # Write your code here
    n = len(q)
    bribes = [0] * n
    for i in range(n):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes[q[j] - 1] += 1
    print(sum(bribes))
q = [2,1,5,4,3]
print(minimumBribes(q))