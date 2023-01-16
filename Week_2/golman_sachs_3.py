# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)

n = 3
res = str(fact(n))
cnt = 0
r = len(res)-1
while r > -1:
    if res[r] == "0":
        cnt += 1
    else:
        print(cnt)
        break
    r -= 1

# -By Sakshi Aherkar
