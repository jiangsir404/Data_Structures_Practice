import java.util.Arrays;

public class Example {
    public static void main(String[] args){
        Solution s = new Solution();
        int[] nums = {3, 2, 4};
        int target = 6;

        int[] res = s.twoSum(nums, target);
        System.out.println(Arrays.toString(res));
    }
}

/*
解题思路: 双指针法推进。
1. 先排序； 设置两个指针i,j想中间推进，循环条件为while(i<j);
2. 如果nums[i] + nums[j]=target, 退出循环，如果>target, j--, 如果<target, i++;
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1;
        int[] bak = nums;
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums)+" "+Arrays.toString(bak));
        while(i<j){
            if(nums[i] + nums[j] == target) {
                return new int[] {nums[i], nums[j]};
            }else if(nums[i] + nums[j] > target){
                j --;
            }else{
                i ++;
            }
        }
        return new int[] {-1, -1};
    }
}