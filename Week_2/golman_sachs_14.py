# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [42,11,1,97]
# Output: 2
def countNicePairs(nums) -> int:
        res = 0
        count = collections.Counter()
        for a in nums:
            b = int(str(a)[::-1])
            res += count[a - b]
            count[a - b] += 1
        return res % (10**9 + 7)
                
        print(cnt)
        return cnt
nums = [42,11,1,97]
res = countNicePairs(nums)
print(res)
