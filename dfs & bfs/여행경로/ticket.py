from collections import defaultdict
# defaultdict 풀이
def solution(tickets):
    r = defaultdict(list)
    
    for a, b in tickets:
        r[a].append(b)
    for i in r.keys():
        r[i].sort()
    print(r)
    
    stack = ["ICN"]
    ans = []
    
    while stack:
        q = stack[-1]
        if r[q] != []:
            stack.append(r[q].pop(0))
        else:
            ans.append(stack.pop())
        print(stack)
    return ans[::-1]
    
        




# from collections import deque

# def dfs(tickets, visited, curr, path, ans):
#     if len(path) == len(tickets) + 1:
#         ans.append(path)
#         return True
#     for i in range(len(tickets)):
#         if tickets[i][0] == curr and not visited[i]:
#             visited[i] = True
#             if dfs(tickets, visited, tickets[i][1], path + [tickets[i][1]], ans):
#                 return True
#             visited[i] = False
    
    
# def solution(tickets):
#     n = len(tickets)
#     visited = [False] * n
    
#     tickets.sort()
#     ans = []
#     dfs(tickets, visited, "ICN", ["ICN"], ans)
#     return ans[0]
    
    
    