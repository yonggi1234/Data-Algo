def dfs(numbers, target, i, s): 
    global ct

	
    if i == len(numbers):
        if s == target: 
            ct += 1
        return 
    n = numbers[i]
    dfs(numbers, target, i + 1, s + n)  
    dfs(numbers, target, i + 1, s - n)

def solution(numbers, target) : 
 	
    global ct
    ct = 0 
    dfs(numbers, target, 0, 0)
    
    return ct

# dp를 통한 풀이
# def solution(numbers, target):
#     l = len(numbers)
#     dp = [[] for _ in range(l + 1)]
#     dp[0].append(0)
#     for i in range(l):
#         num = numbers[i]
        
#         for j in dp[i]:
#             dp[i + 1].append(j + num)
#             dp[i + 1].append(j - num)
    
#     ct = 0
#     for i in dp[l]:
#         if i == target:
#             ct += 1
#     return ct