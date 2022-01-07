class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = defaultdict(list)
        for i, n in enumerate(nums):
            self.d[n].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return self.d[target][random.randrange(0, len(self.d[target]))]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)