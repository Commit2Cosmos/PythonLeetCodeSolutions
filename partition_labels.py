from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = [float('inf')] * 26
        res = []


        for i in range(len(s)):
            last_seen[ord(s[i])-97] = i

        size = 1
        end = 0

        for i in range(len(s)):
            if end < last_seen[ord(s[i])-97]:
                end = last_seen[ord(s[i])-97]
            
            if i == end:
                res.append(size)
                size = 0
            
            size += 1

        return res



s = "vhaagbqkaq"


sol = Solution()
print(sol.partitionLabels(s))