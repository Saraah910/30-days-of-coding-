# You are given two 0-indexed integer arrays nums1 and nums2, each of size n, and an integer diff. Find the number of pairs (i, j) such that:

# 0 <= i < j <= n - 1 and
# nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
# Return the number of pairs that satisfy the conditions.

 

# Example 1:

# Input: nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
# Output: 3

from sortedcontainers import SortedList

def numberOfPairs(nums1,nums2,diff):
    sorted_list = SortedList()
    count = 0
	
	for a, b in zip(nums1, nums2):
	    reduced_array.append(a-b)
    for num in reduced_array:
        smaller = sorted_list.bisect_right(num + diff)
        count += smaller
		
		sorted_list.add(num)
        
    return count
    
nums1 = [3,2,5]
nums2 = [2,2,1]
diff = 1

result = numberOfPairs(nums1,nums2,diff)
print(result)

# -By Sakshi Aherkar
