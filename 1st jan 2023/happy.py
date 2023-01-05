# A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

# Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

 

# Example 1:

# Input: s = "level"
# Output: "l"
def longestPrefix( s: str) -> str:
        
    base, MOD = 29, pow(2,31)-1
    
    lookup = []
    seed, n = 1, len(s)
    for i in range(n):
        lookup.append(seed)
        seed *= base
        seed %= MOD
    
    result, prefix, suffix = "", 0, 0
    for i in range(n-1):
        prefix *= base
        prefix += ord(s[i])-ord('a')
        prefix %= MOD
        suffix += (ord(s[n-1-i])-ord('a'))*lookup[i]
        suffix %= MOD
        if prefix == suffix:
            result = s[:i+1]
    return result
    
s = "level"
res = longestPrefix(s)
print(res)
