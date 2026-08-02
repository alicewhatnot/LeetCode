class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] newNums = new int[nums.length];
        int index = 0;

        for (int num : nums) {
            if (num < pivot) {
                newNums[index] = num;
                index++;
            }
        }
        for (int num : nums) {
            if (num == pivot) {
                newNums[index] = num;
                index++;
            }
        }
        for (int num : nums) {
            if (num > pivot) {
                newNums[index] = num;
                index++;
            }
        }

        return newNums;
    }
}