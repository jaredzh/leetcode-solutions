class Solution:
    def numberOfWays(self, s: str) -> int:
        d = {"0": 0, "01": 0, "010": 0, 
             "1": 0, "10": 0, "101": 0}
        
        for val in s:
            if val == "0":
                d["0"] += 1
                d["010"] += d["01"]
                d["10"] += d["1"]
            else:
                d["1"] += 1
                d["101"] += d["10"]
                d["01"] += d["0"]
        return d["010"] + d["101"]