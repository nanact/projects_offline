def count_money_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]

amount = 5
print("Ways to divide money:", count_money_partitions(amount))