class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        i = 0
        while i < len(goal):
            if s == goal:
                return True
            # rotate
            goal = goal[1:] + goal[0]
            i += 1
        return False
