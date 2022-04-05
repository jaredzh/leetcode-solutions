class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr_t = 60*int(current[0:2]) + int(current[3:5])
        target_t = 60*int(correct[0:2]) + int(correct[3:5])
        
        diff = target_t - curr_t
        res = 0
        for t in [60, 15, 5, 1]:
            res += (diff // t)
            diff %= t
        return res