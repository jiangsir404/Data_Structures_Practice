import java.util.Arrays;

public class MoveZeroes {
    public static void main(String[] args){
        Solution s = new Solution();
        int[] nums = {1,3,5,6};
        int val = 0;
        int res = s.searchInsert1(nums, val);
        System.out.println(res);
    }
}

/*解题思路: 快慢指针
1. 遍历数组, 如果nums[i] !=val nums[j]=nums[i], j++;
*/
class Solution {
    // 用时0s, 击败了100%
    public int searchInsert(int[] nums, int target) {
        // 需要处理好左边界和右边界值。
        if(nums.length == 0){
            return 0;
        }
        if(nums[nums.length-1] < target){
            return nums.length;
        }
        int left = 0;
        int right = nums.length - 1;
        while(left < right){
            int mid = left + (right-left) / 2;
            if(nums[mid] < target){
                left = mid + 1;
            }else{
                right = mid;
            }
        }

        return left;
    }

    // 用时0s, 击败了6.66%
    public int searchInsert1(int[] nums, int target) {
        使用Arrays自带的binarySearch()函数
        int res = Arrays.binarySearch(nums, target);
        System.out.println(res);
        // 如果不存在值，binarySearch函数返回的是(-(insertPoint)-1)
        if(res < 0){
            res = res * (-1) - 1;
        }
        return res;
    }
}