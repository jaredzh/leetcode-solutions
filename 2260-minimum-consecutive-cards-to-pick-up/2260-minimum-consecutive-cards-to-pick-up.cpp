class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        unordered_map<int, int> m;
        int res = INT_MAX;
        
        for(int i = 0; i < cards.size(); ++i) {
            int v = cards[i];
            if(m.find(v) != m.end()) {
                res = min(res, i - m[v] + 1);
            }
            m[v] = i;
        }
        
        return res == INT_MAX ? -1 : res;
    }
};