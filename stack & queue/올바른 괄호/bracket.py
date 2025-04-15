from collections import deque
def solution(s):
    queue = deque()
    
    for i in s:
        if i == "(":
            queue.append(True)
        else:
            try:
                queue.pop()
            except:
                return False
    return len(queue) == 0