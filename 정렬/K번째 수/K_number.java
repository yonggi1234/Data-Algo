import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int k = 0; k < commands.length; k ++){
            int[] arr = new int[commands[k][1] - commands[k][0] + 1];
            
            for(int i = 0; i < commands[k][1] - commands[k][0] + 1; i++){
                arr[i] = array[i + commands[k][0] - 1];
            }
            Arrays.sort(arr);
            for(Integer e : arr)
                System.out.printf("%d ", e);
            System.out.println();
            answer[k] = arr[commands[k][2] - 1];
        }
        
        return answer;
    }
}