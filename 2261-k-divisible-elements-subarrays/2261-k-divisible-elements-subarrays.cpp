class Solution {
public:
    int countDistinct(vector<int>& nums, int k, int p) {
        set<vector<int>> s;
        int n = nums.size();
        for(int i = 0; i < n; ++i) {
            vector<int> v;
            int ct = 0;
            for(int j = i; j < n; ++j) {
                if (nums[j]%p == 0) {
                    ++ct;
                }
                v.push_back(nums[j]);
                if (ct <= k) {
                    s.insert(v);
                } else {
                    break;
                }
            }
        }
        return s.size();
    }
};