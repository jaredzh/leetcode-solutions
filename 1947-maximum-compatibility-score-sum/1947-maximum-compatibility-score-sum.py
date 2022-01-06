class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        self.res = 0
        def helper(s, m):
            res = 0
            for i in range(len(s)):
                for j in range(len(s[i])):
                    if s[i][j] == m[i][j]:
                        res += 1
            return res
        
        def dfs(path, stud):
            if len(path) == len(students):
                self.res = max(self.res, helper(path, mentors))
            for i in range(len(stud)):
                dfs(path+[stud[i]], stud[:i]+stud[i+1:])
        
        dfs([], students)
        return self.res