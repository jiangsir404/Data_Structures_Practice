import java.util.*;

/**
 * @author rivir
 * @date 2020/3/25
 * 136. 只出现一次的数字 https://leetcode-cn.com/problems/single-number/
 */

public class singleNumber{
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {2,2,1};
        int res = s.singleNumber(nums);
        System.out.println(res);
    }
}

class Solution {
    public int singleNumber(int[] nums) {
        int ret = 0;
        Map<Integer, Integer> m = new HashMap<>();
        for(int i: nums){
            if(m.containsKey(i)){
                m.put(i, m.get(i) + 1);
            }else{
                m.put(i, 1);
            }
        }
        for(Map.Entry<Integer, Integer> entry: m.entrySet()){
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if(value == 2){
                ret = key;
            }
        }
        return ret;
    }
}