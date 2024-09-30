"""
Given a 6 x 6 2D Array, arr:

#=============#
# 1 1 1 0 0 0 #
# 0 1 0 0 0 0 #
# 1 1 1 0 0 0 #
# 0 0 0 0 0 0 #
# 0 0 0 0 0 0 #
# 0 0 0 0 0 0 #
#=============#

An hourglass in A is a subset of values with indices 
falling in this pattern in arr's graphical representation:

#=======#
# A B C #
#   D   #
# E F G #
#=======#

There are 16 hourglasses in arr. 
An hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in arr, 
then print the maximum hourglass sum. 
The array will always be 6 x 6.
"""
def hourglassSum(arr):
    """Calculates the maximum hourglass sum in a 2D array.

    Args:
        arr: A 6x 6 2D array representing the hourglass grid.

    Returns:
        The maximum hourglass sum.
    """
    upper = []
    middle = []
    lower = []
    sum_store = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            upper.append(arr[i][j:j+3])
            middle.append(arr[i+1][j+1])
            lower.append(arr[i+2][j:j+3])
    for i in range(len(upper)):
        sum_store.append(sum(upper[i])+ middle[i] + sum(lower[i])) 
    return max(sum_store)

if __name__ == '__main__':
    row = []
    # Input list of integer with length 6
    # example input : 1,2,3,4,5,6 (repeat for 6 times)
    for i in range(6):
        row.append(
            list(map(
                int,list(input().split(',')))
            ))
    print(hourglassSum(row))
