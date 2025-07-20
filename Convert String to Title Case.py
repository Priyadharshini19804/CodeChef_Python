"""
Given a string S consisting of only lowercase and uppercase English letters and spaces, 
your task is to convert it into title case. In title case, the first letter of each word is capitalized while the rest are in lowercase, 
except for words that are entirely in uppercase (considered as acronyms), which should remain unchanged.

Input Format
The first line contains a single integer T, the number of test cases.
Each of the next T lines contains a string S.

Output Format
For each test case, print a single line containing the string S converted into title case.

Input
5
hello world
this is a CODECHEF problem
WELCOME to the JUNGLE
the quick BROWN fOx
programming in PYTHON

Output
Hello World
This Is A CODECHEF Problem
WELCOME To The JUNGLE
The Quick BROWN Fox
Programming In PYTHON

"""

n = int(input())
for _ in range(n):
    line = input().split()
    result = []
    for word in line:
        if word.isupper():  # leave it unchanged
            result.append(word)
        else:
            result.append(word.capitalize())
    print(' '.join(result))
