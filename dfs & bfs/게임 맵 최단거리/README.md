* 난이도: Lv 3
* 문제: https://school.programmers.co.kr/learn/courses/30/lessons/1844

풀이 과정
1. bfs는 LIFO(queue.pop()) 을 사용하고, dfs는 FIFO(queue.popleft()) 를 사용함
2. 따라서 해당 문제에서 visited 리스트를 통해 굳이 방문 여부 체크 안해도 되는 문제였음