class Solution {
    public int minimumOperations(int[] nums) {
        int ans = 0;

        for (int num : nums) {
            ans += (num % 3 == 0 ? 0 : 1);
        }

        return ans;
    }
}