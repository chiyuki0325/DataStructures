"""
https://leetcode.cn/problems/generate-parentheses/solutions/9251
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 按照题解编写的递推（？）法

        combinations: List[List[str]] = [[""], ["()"]]
        if n < 2:
            return combinations[n]

        for i in range(2, n+1):
            combinations.append([])
            for p in range(i):  # 0~i-1
                q = i-1-p
                for comb_p in combinations[p]:
                    for comb_q in combinations[q]:
                        combinations[i].append("("+comb_p+")"+comb_q)

        return combinations[n]


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
