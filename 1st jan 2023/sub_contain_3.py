# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
def numberOfSubstrings(s):
    res = i = 0
    count = {c: 0 for c in 'abc'}
    for j in range(len(s)):
        count[s[j]] += 1
        while all(count.values()):
            count[s[i]] -= 1
            i += 1
        res += i
    return res
    
s = "abcabc"
res= numberOfSubstrings(s)
print(res)


# -By Sakshi Aherkar
