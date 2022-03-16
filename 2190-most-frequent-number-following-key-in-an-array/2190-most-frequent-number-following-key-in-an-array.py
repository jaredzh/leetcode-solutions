class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        d = defaultdict(int)
        for i in range(len(nums)-1):
            if nums[i] == key:
                d[nums[i+1]] += 1
        return max(d, key=d.get)