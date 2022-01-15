class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        G = defaultdict(list)
        neq = []
        for eq in equations:
            a, b = eq[0], eq[-1]
            if eq[1] == "!":
                if a == b:
                    return False
                neq.append([a, b])
            elif a != b:
                G[a].append(b)
                G[b].append(a)
        
        
        def can_meet(u, v, seen):
            if u == v:
                return True
            seen.add(u)
            for node in G[u]:
                if node not in seen and can_meet(node, v, seen):
                    return True
            return False
        
        for u, v in neq:
            if can_meet(u, v, set()):
                return False
        return True