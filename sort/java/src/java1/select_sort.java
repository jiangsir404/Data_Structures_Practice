package java1;
import java.util.Arrays;

public class select_sort {
	public static void main(String[] args) {
		int[] nums = {1, 3, 5, 7, 9, 2, 4, 6, 8, 0};
		for(int i=0; i<nums.length-1; i++) {
			int min = i; //记录最小值
			// 第二重循环j的范围为j+1-length,划分左有序区间和右无序区间
			for(int j=i+1; j<nums.length; j++) {
				if(nums[j] < nums[min]) {
					min = j;
				}
			}
			//如果min == i, 则无需交换
			if(min != i) {
				int tmp = nums[min];
				nums[min] = nums[i];
				nums[i] = tmp;
			}
			System.out.println(Arrays.toString(nums));
		}
	}
}