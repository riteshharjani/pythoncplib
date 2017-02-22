"""
http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists
"""

def lis(arr):
    n = len(arr)
    lis = [1]*n

    for i in xrange(n):
        for j in xrange(i):
            #print "i, j, lis", i, j, lis, lis[i], lis[j]
            if (arr[i] > arr[j] and (lis[i] < (lis[j] + 1))):
                lis[i] = lis[j] + 1

    print lis
    return max(lis[:n])

def main():
    arr = [10, 22, 9, 33, 21, 50, 41, 49, 8]
    print lis(arr)

main()
