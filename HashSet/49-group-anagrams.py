from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in groups:
                groups[sorted_string].append(string)
            else:
                groups[sorted_string] = [string]
        return list(groups.values())
