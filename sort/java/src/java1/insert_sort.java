package java1;
import java.util.Arrays;

public class insert_sort {
	public static void main(String[] args) {
		int[] nums = {1, 3, 5, 7, 9, 2, 4, 6, 8, 10};
		
		if(nums.length <= 1) {;}
		for(int i=1; i<nums.length; i++) {
			int j = 0;
			int val = nums[i]; //保存需要比较的元素，否则搬移的时候会被覆盖
			for(j=i-1; j>=0; j--) {
				if(nums[j] > val) {
					nums[j+1] = nums[j]; //数据搬移
				}else {
					break;
				}
			}
			nums[j+1] = val;
			System.out.println(Arrays.toString(nums));
		}
	}
}