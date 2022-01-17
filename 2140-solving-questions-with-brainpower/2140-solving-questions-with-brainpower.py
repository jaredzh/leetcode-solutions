class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0] * n
        maxes = [0] * (n+1)
        for i in range(n-1, -1, -1):
            val, k = questions[i]
            if k+i+1 >= n:
                dp[i] = val
            else:
                dp[i] = maxes[k+i+1] + val
            maxes[i] = max(maxes[i+1], dp[i])
        return max(dp)