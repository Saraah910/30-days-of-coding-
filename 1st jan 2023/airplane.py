# n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. 
# But after that, the rest of the passengers will:

# Take their own seat if it is still available, and
# Pick other seats randomly when they find their seat occupied
# Return the probability that the nth person gets his own seat.

 

# Example 1:

# Input: n = 1
# Output: 1.00000

def nthPersonGetsNthSeat(n):
    return 1.0 if n == 1 else 0.5
    
n = 1
res = nthPersonGetsNthSeat(n)
print(res)

# -By Sakshi Aherkar
