

# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
  
  
from collections import Counter

def getHint(secret, guess):
    lookup = Counter(secret)
    
    x, y = 0, 0
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            x+=1
            lookup[secret[i]]-=1

    for i in range(len(guess)):
        if guess[i] in lookup and secret[i] != guess[i] and lookup[guess[i]]>0:
            y+=1
            lookup[guess[i]]-=1
	
    return "{}A{}B".format(x, y)
    
secret = input()
guess = input()

result = getHint(secret,guess)
print(result)


# -By Sakshi Aherkar 
