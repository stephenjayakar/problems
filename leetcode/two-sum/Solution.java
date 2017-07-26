/* Given nums = [2, 7, 11, 15], target = 9,
   
   Because nums[0] + nums[1] = 2 + 7 = 9,
   return [0, 1]
*/

public class Solution {
    public int[] twoSum(int[] nums, int target) {
	for (int i = 0; i < nums.length; i++) {
	    for (int j = i + 1; j < nums.length; j++) {
		if (nums[i] + nums[j] == target) {
		    return new int[]{i, j};
		}
	    }
	}
    }

    // The test
    public static void main(String[] args) {
	int[] nums = {2, 7, 11, 15};
	int target = 9;
	int[] answer = twoSum(nums, target);

	System.out.println(Arrays.toString(answer));
    }
}
