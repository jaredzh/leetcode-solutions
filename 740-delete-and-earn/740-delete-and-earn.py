class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        d = defaultdict(int)
        
        for n in nums:
            d[n] = n*c[n]
        
        points = []
        for i in range(1, max(nums)+1):
            if i in d:
                points.append(d[i])
            else:
                points.append(0)
        if len(points) == 1:
            return points[0]
        elif len(points) == 2:
            return max(points)

        dp = [0]*len(points)
        dp[0] = points[0]
        dp[1] = max(points[0:2])
        print(points)
        for i in range(2, len(points)):
            dp[i] = max(dp[i-1], points[i]+dp[i-2])
        print(dp)
        return dp[-1]
        