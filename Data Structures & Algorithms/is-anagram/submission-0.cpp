class Solution {
public:
    bool isAnagram(string s, string t) {

        int n = s.length();

        if (n != t.length()) {
            return false;
        }

        unordered_map<char, int> sMap;

        for (int i = 0; i < n; i++) {
            if (sMap.find(s[i]) != sMap.end()) {
                sMap[s[i]]++;
            }
            else {
                sMap[s[i]] = 1;
            }
        }

        for (int j = 0; j < n; j++) {
            if (sMap.find(t[j]) != sMap.end()) {
                if (sMap[t[j]] > 0) {
                    sMap[t[j]]--;
                }
                else {
                    return false;
                }
            }
            else {
                return false;
            }
        }

        return true;


    }
};
