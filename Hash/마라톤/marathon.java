import java.util.*;
import java.util.Map.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for(int i = 0; i < participant.length; i++){
            if(map.containsKey(participant[i])){
                int ct = map.get(participant[i]);
                map.put(participant[i], ct + 1);
            }
            else
                map.put(participant[i],1);
        }
        for(int i = 0; i < completion.length; i++){
            String p = completion[i];
            int ct = 0;
            if (map.get(p) > 1){
                ct = map.get(p) - 1;
                map.put(p, ct);
            }
            else
                map.remove(p);
        }
        System.out.println(map);
        for(Map.Entry<String, Integer> entry : map.entrySet()){
            if (entry.getValue() > 0)
                return entry.getKey();
        }
        return answer;
    }
}