class Solution2:
    # O(n^2)，过不了
    def findTheLongestSubstring(self, s: str) -> int:
        indexes = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        pfx: list[int] = []  # list[mask]

        for char in s:
            if not pfx:
                pfx.append(0)
            else:
                pfx.append(pfx[-1])
            index = indexes.get(char, -1)
            if index != -1:
                pfx[-1] ^= 1 << index

        # print(list(bin(i) for i in pfx))
        length = 0

        def meet(l, r) -> bool:
            pfx_l = pfx[l - 1] if l > 0 else 0
            return pfx[r] ^ pfx_l == 0

        for right in range(len(s)):
            for left in range(right + 1):
                if meet(left, right):
                    length = max(length, right - left + 1)

        # print(length)
        return length


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        indexes = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        first_seen = {0: -1}  # dict[mask, left]
        # 住手，这已经不是前缀和了

        length = 0
        mask = 0

        for right in range(len(s)):
            char = s[right]
            index = indexes.get(char)
            if index is not None:
                mask ^= 1 << index

            if mask in first_seen:
                left = first_seen[mask]
                length = max(length, right - left)
            else:
                first_seen[mask] = right

        return length


if __name__ == "__main__":
    assert Solution().findTheLongestSubstring("eleetminicoworoep") == 13
    assert Solution().findTheLongestSubstring("leetcodeisgreat") == 5
    assert Solution().findTheLongestSubstring("bcbcbc") == 6
