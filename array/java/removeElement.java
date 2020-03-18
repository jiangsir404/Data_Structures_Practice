import java.util.Arrays;

public class MoveZeroes {
    public static void main(String[] args){
        Solution s = new Solution();
        int[] nums = {3,2,2,3};
        int val = 3;
        int res = s.removeElement(nums, val);
        System.out.println(res);
    }
}

/*解题思路: 快慢指针
1. 遍历数组, 如果nums[i] !=val nums[j]=nums[i], j++;
*/
class Solution {
    public int removeElement(int[] nums, int val) {
        int j = 0;
        for(int i=0;i<nums.length;i++){
            if (nums[i] != val){
                nums[j++] = nums[i];
            }
        }
        return j;
    }
}