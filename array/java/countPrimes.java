
//204. 计数质数

/*
算法思路:
1. 首先从 2 开始，我们知道 2 是一个素数，那么 2 × 2 = 4, 3 × 2 = 6, 4 × 2 = 8... 都不可能是素数了。
2. 然后我们发现 3 也是素数，那么 3 × 2 = 6, 3 × 3 = 9, 3 × 4 = 12... 也都不可能是素数了。这样通过刷选排除来的就是[2,n)之间的所有素数了。
*/

import java.util.Arrays;

public class Solution {
    public int countPrimes(int n) {
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);
        int count=0;

        for(int i=2; i*i<n; i++){
            for (int j=i*i; j<n; j+=i){
                isPrime[j] = false;
            }
        }
        for(int i=2;i<n;i++){
            if(isPrime[i]){
                count ++;
            }
        }
        return count;

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int res = s.countPrimes(10);
        System.out.println(res);
    }
}