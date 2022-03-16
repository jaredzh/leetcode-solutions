class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        mapped = []
        for i, n in enumerate(nums):
            k = ""
            for s in str(n):
                k += str(mapping[int(s)])
            mapped.append((int(k), i))
        return [x for _, x in sorted(zip(mapped, nums), key=lambda pair: pair[0])]