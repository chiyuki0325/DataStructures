from typing import List
from functools import cache


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        @cache
        def last_appeared_pos(char: str) -> int:
            for i in range(len(s)-1, -1, -1):
                if s[i] == char:
                    return i

        result = []
        lbound = 0

        while lbound < len(s):
            rbound = lbound
            # 寻找一个字符以更新，比如第一个字符是 a
            check_pos = lbound
            checked_chars = set()
            while check_pos < rbound or not checked_chars:
                char = s[check_pos]
                if char not in checked_chars:
                    checked_chars.add(char)
                    # 寻找 a 最后一个出现的位置，更新 rbound
                    rbound = max(rbound, last_appeared_pos(s[check_pos]))
                check_pos += 1
                # 换下一个字符继续延展

            # print(lbound, rbound)
            # print(s[lbound:rbound+1])
            result.append(rbound-lbound+1)

            lbound = rbound+1

        return result


if __name__ == "__main__":
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert Solution().partitionLabels("caedbdedda") == [1, 9]
