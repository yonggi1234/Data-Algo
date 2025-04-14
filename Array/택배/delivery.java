package Array.택배;

class Solution {
    //n: 박스 개수, w: 가로 수 , num: 박스 번호
    
    public int solution(int n, int w, int num) {
        int [][] arr = new int[n / w + 2][w + 1];
        int floor = n / w;
        int row = 0;
        int col = 0;
        int max_col = 0;
        int ct = 1;
        for(int i = 1; i < floor + 2; i++){
            for(int j = 1; j < w + 1; j++){
                if((i - 1) * w + j > n)
                    break;
                if(i % 2 == 1)
                    arr[i][j] = ct;
                else
                    arr[i][w - j + 1] = ct;
                if (ct == num){
                    if(i % 2 == 1)
                        col = j;
                    else
                        col = w - j + 1;
                }
                ct += 1;
            }
        }
        int ans = 0;
        for (int i = floor + 1; i >= 0; i--){
            if(arr[i][col] != 0)
                ans += 1;
            
            if(arr[i][col] == num)
                break;
                
        }
        return ans;
        
        
//         for (int i = 0; i < arr.length; i++) {
//             int[] inArr = arr[i];            
//             for (int j = 0; j < inArr.length; j++) {
//                 System.out.print(inArr[j] + " ");
//             }            
//             System.out.println();
//         }    
    
        
    }
}