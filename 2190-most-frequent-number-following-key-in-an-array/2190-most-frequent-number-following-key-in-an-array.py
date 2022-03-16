class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        d = defaultdict(int)
        for target in range(1, 1001):
            for i in range(len(nums)-1):
                if nums[i]==key and nums[i+1]==target:
                    d[target]+=1
        return max(d, key=d.get)