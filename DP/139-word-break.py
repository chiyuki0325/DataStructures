from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 暴力穷举法+缓存
        cache = {}

        def dfs(substring: str) -> bool:
            if substring in cache:
                return cache[substring]
            if len(substring) == 0:
                return True
            result = False
            for word in wordDict:
                if substring.startswith(word):
                    result = result or dfs(substring[len(word):])
            cache[substring] = result
            return result

        return dfs(s)


# 不是，怎么暴力加了个缓存就过了，我还没优化成动态规划呢


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 尝试优化：减小缓存的维度
        # “合一维”
        # 代价：牺牲可读性

        # 时间已经击败 100% 了，但不是动态规划，还要继续优化吗

        word_set = set(wordDict)
        word_len_set = set(map(len, wordDict))
        total_len = len(s)

        # 状态定义：[1, i] 子串是否可以用 word_set 中的词拼成
        state = [False] * (total_len + 1)
        state[0] = True

        def dfs(l: int):
            if l == total_len:
                return
            for word_len in word_len_set:
                new_l = l+word_len
                if new_l <= total_len and not state[new_l] and s[l:new_l] in word_set and state[l]:
                    state[new_l] = True
                    dfs(new_l)

        dfs(0)
        return state[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划：时间内存双赢的解决方案

        word_set = set(wordDict)
        word_len_set = set(map(len, wordDict))
        total_len = len(s)

        state = [False] * (total_len + 1)
        state[0] = True

        for r in range(1, total_len+1):
            for word_len in word_len_set:
                l = r-word_len
                if l >= 0 and not state[r] and s[l:r] in word_set and state[l]:
                    state[r] = True
        return state[-1]
