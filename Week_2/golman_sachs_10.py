def peopleAwareOfSecret(n, delay, forget) -> int:

        dp, ct = [0] * n, 0
        dp[0] = 1

        for i in range(1, n):

            dp[i] = ct + dp[i-delay] - dp[i-forget]
            ct = dp[i]

        return sum(dp[n-forget:]) % 1000000007

n = 6
delay = 2
forget = 4
res = peopleAwareOfSecret(n,delay,forget)
print(res)
