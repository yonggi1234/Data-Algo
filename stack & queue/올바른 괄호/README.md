* 난이도: Lv 2
* 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42586

풀이 과정
1. 단순히 stack으로 푸는 문제
2. 처음엔 지역변수 선언 후, 괄호 열고 닫을 때마다 더하고 빼 최종적으로 0인지 확인했지만
stack 사용 후, try-except를 통해 에러가 발생할 경우 return False로 처리해 더 간결해짐