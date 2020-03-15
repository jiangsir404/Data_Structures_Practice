import java.util.Arrays;

public class MoveZeroes {
    public static void main(String[] args){
        Solution s = new Solution();
        int[] nums = {0,1};
        s.moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}

/*解题思路: 快慢指针
1. 遍历数组, 如果nums[i] !=0 nums[j]=nums[i], j++;
2. 如果i != j, nums[i] = 0;*/
class Solution {
    public void moveZeroes(int[] nums) {
        if(nums.length <= 1){ return;}
        int j = 0; // 慢指针
        for(int i=0;i<nums.length;i++){
            if(nums[i] != 0){
                nums[j] = nums[i];
                if(i != j){
                    nums[i] = 0;
                }
                j ++;
            }

        }
    }
}