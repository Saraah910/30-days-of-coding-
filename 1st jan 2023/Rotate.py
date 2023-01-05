# You are given an integer array nums of length n.

# Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

# F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
# Return the maximum value of F(0), F(1), ..., F(n-1).

# The test cases are generated so that the answer fits in a 32-bit integer.


# Example 1:

# Input: nums = [4,3,2,6]
# Output: 26

def maxRotateFunction(nums):
    
    s=sum(nums)

    d=sum(elem * idx for idx, elem in enumerate(nums)) 
    sol = d
    for pivot in range(len(nums)-1,-1,-1): 
        d+=s-len(nums)*nums[pivot] 
        sol=max(d,sol)
    return sol
 
nums = [4,3,2,6]   
result = maxRotateFunction(nums)
print(result)



# -By Sakshi Aherkar
