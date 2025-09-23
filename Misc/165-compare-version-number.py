from typing import Literal


class Solution:
    def compareVersion(self, version1: str, version2: str) -> Literal[1, 0, -1]:
        version1_arr = version1.split(".")
        version2_arr = version2.split(".")

        len1 = len(version1_arr)
        len2 = len(version2_arr)

        if len1 < len2:
            version1_arr += [0]*(len2-len1)
            length = len2
        else:
            version2_arr += [0]*(len1-len2)
            length = len1

        for i in range(length):
            subversion1 = int(version1_arr[i])
            subversion2 = int(version2_arr[i])
            if subversion1 > subversion2:
                return 1
            elif subversion1 < subversion2:
                return -1

        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.compareVersion("3.9", "3.11") == -1
    assert s.compareVersion("3.7.1", "3.6.10") == 1
    assert s.compareVersion("3.12", "3.12.0") == 0
    assert s.compareVersion("1", "1.0.1") == -1
