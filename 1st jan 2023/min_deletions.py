# You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.

# Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.

# Note that an integer x divides y if y % x == 0.

 

# Example 1:

# Input: nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]
# Output: 2

import math
def minOperations(nums, numsDivide) -> int:

        d = {}
        for i in nums:
            if i not in d:
                d[i]= 1
            else:
                d[i]+=1
		
        nums = list(d.keys())
        nums.sort()
        cnt = 0
		
        def GcdOfArray(arr, idx):
            if idx == len(arr)-1:
                return arr[idx]

            a = arr[idx]
            b = GcdOfArray(arr,idx+1)

            return math.gcd(a, b)
        gcd = GcdOfArray(numsDivide,0)
        ans = 0
		
        for ele in nums:
            if gcd%ele==0:
                ans = ele
                break
            else:
                cnt+=d[ele]
        if ans==0:
            return -1
        else:
            return cnt
            
nums = [2,3,2,4,3]
numsDivide = [9,6,9,3,15]
res = minOperations(nums,numsDivide)
print(res)


# -By Sakshi Aherkar
