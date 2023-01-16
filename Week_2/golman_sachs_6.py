# Que: You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

 

# Example 1:

# Input: cards = [3,4,2,3,4,7]
# Output: 4

from collections import defaultdict
def minimumCardPickup(cards) -> int:
    mini = float("+inf")

    dict = defaultdict(list)

    for i in range(len(cards)):
        dict[cards[i]].append(i)
        
        if len(dict[cards[i]]) > 1:
            diff = dict[cards[i]][-1] - dict[cards[i]][-2]
            mini = min(mini, diff)
        else:
            continue
    print(dict)

    if mini == float("+inf"):
        return -1
    return mini + 1
    
cards = [3,4,2,3,4,7]
res = minimumCardPickup(cards)
print(res)

-By Sakshi Aherkar
