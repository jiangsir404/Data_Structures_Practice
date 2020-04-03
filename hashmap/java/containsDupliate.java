import java.util.*;

/**
 * @author rivir
 * @date 2020/3/25
 * 217. 存在重复元素 https://leetcode-cn.com/problems/contains-duplicate/
 */

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> m = new HashSet<>();
        for(Integer i: nums){
            if(m.contains(i)){
                return true;
            }else{
                m.add(i);
            }
        }
        return false;
    }
}