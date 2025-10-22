from typing import List


class Solution:
    def is_palindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        # 优化过后的递推法
        results: List[List[List[str]]] = [[[]], [[s[0]]]]
        # 索引为字符串长度

        for end in range(2, len(s) + 1):
            results.append([])
            combs = results[end]

            # 枚举所有后缀
            for suffix_len in range(1, end + 1):
                suffix = s[:end][-suffix_len:]
                # print("suffix", suffix_len, suffix)
                if self.is_palindrome(suffix):
                    # 如果新的后缀是回文字符串
                    # 那么就复用之前的结果，加上新的后缀
                    # print("last_combs", end - suffix_len, results[end - suffix_len])
                    for last_comb in results[end - suffix_len]:
                        combs.append(last_comb + [suffix])

            # print(end, results)

        return results[len(s)]


if __name__ == "__main__":
    s = Solution()
    assert s.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
