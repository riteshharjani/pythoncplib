"""
http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/
lcs(i,j) = 1 + lcs(i-1,j-1) if (x[i] == y[j]) or
lcs(i,j) = max(lcs(i-1,j), lcs(i,j-1))

Time Normal complexity = O(2**(n+m))
Time complexity with DP = O(n*m)
space complexity = O(n*m) => this can be further reduced
check MIT video on dynamic programming with LCS
"""

x = "AGGTAB"
n  = len(x)
y = "GXTXAYB"
m = len(y)
dp = [p[:] for p in [[0] * m] * n]
#print dp

def LCS(x, y, i, j):
    if (i == 0 or j == 0):
        return 0
    if (x[i-1] == y[j-1]):
        return 1 + LCS(x, y, i-1, j-1)
    else:
        return max(LCS(x,y,i-1,j), LCS(x,y,i,j-1))

def lcsdp(x,y,i,j):
    if (i == 0 or j == 0):
        return dp[0][0]
    if (dp[i-1][j-1] == 0):
        if (x[i-1] == y[j-1]):
            dp[i-1][j-1] = 1 + lcsdp(x,y,i-1,j-1)
        else:
            dp[i-1][j-1] = max(lcsdp(x,y,i-1,j), lcsdp(x,y,i,j-1))
    return dp[i-1][j-1]

def main():
    print LCS(x,y, len(x), len(y))
    print lcsdp(x,y, len(x), len(y))

main()