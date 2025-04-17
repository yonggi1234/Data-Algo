import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String ans = "";
        String[] num = new String[numbers.length];
        for(int i = 0; i < numbers.length; i++){
            num[i] = Integer.toString(numbers[i]);
        }
        
        Comparator<String> c = new Comparator<String>() {
        @Override
        public int compare(String a, String b) {
            
            return (b + a).compareTo(a + b);
            }
        };
        Arrays.sort(num, c);
        //람다식 표현
        Arrays.sort(num, (a, b) -> (b + a).compareTo(a + b));
        if (num[0].equals("0"))
            return "0";
        
        for(String e : num)
            ans += e;
        
        return ans;
    }
}