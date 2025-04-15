* 난이도: Lv 1
* 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42576

풀이 과정
1. 입력값 HashMap으로 받아 값 비교 후 일치하는 값 remove, 그 후 남은 값을 return함
2. Array의 값 보려면 for문 돌려야 하지만 HashMap은 그냥 println(hashmap)이 가능
->  HashMap 클래스가 AbstractMap을 상속받고 있고, 
AbstractMap에서 toString()을 통해 내부적으로 반복문 돌리기 때문에 그냥 출력이 된다!