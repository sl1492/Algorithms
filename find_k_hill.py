# Author: Simeng Li
# Divide and Conquer
"""
You’re given an array of n numbers. A hill in this array is an element A[i] that is at least as large as it’s neighbors on either side. In other words, A[i] ≥ A[i − 1] and A[i] ≥ A[i + 1]. (for the boundaries, the first position i = 0 is a hill if a[0] ≥ a[1], resp. the last position i = n − 1
is a hill if a[n − 1] ≥ a[n − 2].) Your goal is to return *some* hill in the array - not every hill of the array.

a k − hill is an element that is at least as large as its k neighbors on each side. 
By this definition, a hill is just a 1 − hill. 
"""

A = [2, 5, 1, 3, 5, 6, 5, 4, 3]
#A = [6, 6, 5, 3]
l = 0
rA = len(A)-1

def find_k_hill(A, l, r, k):
    # base cases:
    if len(A) == 1:
        return A[0]

    # Recursive step
    m = (l + r) // 2
    print(m)
    # m is the first element
    if m == 0:
        if check_k_right(A, m, k):
            return A[m]
    # m is the last element
    elif m == len(A) - 1:
        if check_k_left(A, m, k):
            return A[m]

    # m is less than k and m has more than k right neighbors
    elif m < k and m < len(A)-k:
        if max(A[slice(0, m)]) <= A[m] and check_k_right(A, m ,k):
            return A[m]
    # m is at the tail with less than k elements on the right and m has more than k left neighbors
    elif m > k and m > len(A)-k:
        if max(A[slice(m+1, len(A))]) <= A[m] and check_k_left(A, m, k):
            return A[m]
    # There are no enough numbers both sides
    elif m < k and m > len(A)-k-1:
        print(1)
        if max(A[slice(m+1, len(A))]) <= A[m] and max(A[slice(0, m)]) <= A[m]:
            return A[m]



    elif m >= k and m+k <= len(A) and check_k_left(A, m, k) and check_k_right(A, m, k):
        print(4)
        return A[m]
    elif A[m] < max(A[slice(m-k, m)]):
        print(5)
        return find_k_hill(A, l, m - 1, k)
    elif A[m] < max(A[slice(m, m+k)]):
        print(6)
        return find_k_hill(A, m + 1, r, k)
    else:
        return None


def check_k_left(arr, m, k):
    flag = True
    for i in arr[m-k:m]:
        if i > arr[m]:
            flag = False
    return flag

def check_k_right(arr, m, k):
    flag = True
    for i in arr[m+1:m+k+1]:
        if i > arr[m]:
            flag = False
    return flag


print(find_k_hill(A,0,rA,5))



