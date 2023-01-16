# Que: You are given an integer array nums that is sorted in non-decreasing order.

# Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.

# A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

 

import collections
def isPossible(nums) -> bool:
        
    ones = collections.Counter()
    twos = collections.Counter()
    threes = collections.Counter()

    for i in nums:
        if ones[i-1]>0:
            ones[i-1] -= 1
            twos[i]+=1
            continue

        if twos[i-1]>0:
            twos[i-1] -= 1
            threes[i]+=1
            continue

        if threes[i-1]>0:
            threes[i-1] -= 1
            threes[i]+=1
            continue
        ones[i] += 1

    if ones.total()>0 or twos.total()>0:
        return False
    return True

nums = [1,2,3,3,4,4,5,5]
res = isPossible(nums)
print(res)

# -By Sakshi Aherkar
