class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> numsSet;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (numsSet.find(nums[i]) != numsSet.end()) {
                return true;
            }
            numsSet.insert(nums[i]);
        }

        return false;
    }
};
