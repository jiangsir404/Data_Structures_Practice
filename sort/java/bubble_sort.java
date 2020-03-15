package java1;
import java.util.Arrays;

public class bubble_sort {
	public static void main(String[] args) {
		int[] nums = {4, 5, 6, 3, 2, 1};
		for(int i=0; i<nums.length-1; i++) {
			// 第二重循环j的范围为0-[length-i-1], 划分左无序区间和右有序区间
			for(int j=0; j<nums.length-i-1;j++) {
				// 查找逆序对并且交换
				if(nums[j] > nums[j+1]) {
					int tmp = nums[j+1];
					nums[j+1] = nums[j];
					nums[j] = tmp;
				}
			}
			System.out.println(Arrays.toString(nums));
		}
		
	}
	
}