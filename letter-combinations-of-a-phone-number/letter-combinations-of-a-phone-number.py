class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def helper(idx, path):
            if idx >= len(digits):
                if path:
                    res.append(path)
                return
            for c in d[digits[idx]]:
                helper(idx+1, path+c)
        
        helper(0, "")
        return res