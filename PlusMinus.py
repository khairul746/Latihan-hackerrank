def plusMinus(arr):
    n = len(arr)
    positive = 0
    negative = 0
    null = 0
    for i in arr:
        if i > 0 :
            positive += 1
        elif i < 0 :
            negative += 1
        else :
            null += 1
    print(positive/n)
    print(negative/n)
    print(null/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

