class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        stack, seen, d = [], set(), defaultdict(int)
        
        for i, val in enumerate(s):
            d[val] = i
        
        for i, val in enumerate(s):
            if val not in seen:
                while stack and stack[-1] > val and d[stack[-1]] > i:
                    seen.remove(stack.pop())
                seen.add(val)
                stack.append(val)
        return "".join(stack)