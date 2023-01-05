# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]

def dfs(cur,pos,target):
    if target == 0 and len(cur) == k:
        res.append(cur.copy())
    if target <= 0:
        return
    prev = -1
    for i in range(pos,len(l)):
        if l[i] == prev:
            continue
        cur.append(l[i])
        dfs(cur,i+1,target-l[i])
        cur.pop()
        prev = l[i]
    return res
    
l = [1,2,3,4,5,6,7,8,9]
res = []
n = int(input())
k = int(input())
result = dfs([],0,n)
print(result)
