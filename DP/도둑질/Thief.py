def solution(money):
    l = len(money)
    dp = [0] * l
    dp[0] = money[0]
    dp[1] = money[1]
    dp[2] = money[0] + money[2]
    
    for i in range(3, l - 1):
        dp[i] = max(dp[i - 2], dp[i  - 3]) + money[i]
    ans = max(dp)
    
    
    dp[0] = 0
    dp[2] =money[2]
    for i in range(3, l):
        dp[i] = max(dp[i - 2], dp[i  - 3]) + money[i]
    ans = max(max(dp), ans)
    
    return ans