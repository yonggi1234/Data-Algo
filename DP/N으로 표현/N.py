def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        k = (N * (10 ** i - 1) // 9)
        dp[i].add(k)
        
        for j in range(1, i):
            for m in dp[j]:
                for n in dp[i - j]:
                    dp[i].add(m + n)
                    dp[i].add(m - n)
                    dp[i].add(m * n)
                    if n > 0 and m > 0:
                        dp[i].add(m // n)
        if number in dp[i]:
            return i
    return -1
