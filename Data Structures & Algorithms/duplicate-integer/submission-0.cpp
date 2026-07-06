class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> numsMap;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (numsMap.count(nums[i])) {
                return true;
            }
            else {
                numsMap[nums[i]] = i;
            }
        }

        return false;
    }
};
