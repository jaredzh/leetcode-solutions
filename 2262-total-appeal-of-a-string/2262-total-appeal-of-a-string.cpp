class Solution {
public:
    long long appealSum(string s) {
        long long res = 0;
        long long curr = 0;
        unordered_map<int, int> m;
        for(int i = 0; i < s.size(); ++i) {
            if(m.find(s[i]) == m.end()) {
                curr += (i + 1);
            } else {
                curr += (i - m[s[i]]);
            }
            m[s[i]] = i;
            res += curr;
        }
        return res;
    }
};