"""
Chef has a binary string S of length N.Chef can perform the following operation on S:

Insert any character (0 or 1)at any position in S.

Find the minimum number of operations Chef needs to perform so that no two consecutive characters are same in S.

Input:

3
2
11
4
0101
5
00100

Output:
1
0
2

"""

def solve():
    n = int(input())
    s = input()
    
    ans = 0
    for i in range(n - 1):
        if s[i] == s[i+1]:
            ans += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()
