from itertools import accumulate


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # 前缀和
        # 子数组的和: pfx[r] - pfx[l]
        # 奇数-奇数=偶数
        # 偶数-偶数=偶数
        # 奇数-偶数=奇数
        # 偶数-奇数=奇数

        # 改变思路：存储 pfx[i] 是否为奇数
        pfx_odd = list(n % 2 for n in accumulate(arr))
        # print(pfx_odd)

        # is_odd 数组里有多少个“1-0”或者“0-1”？
        # count（pfx_odd[i]=1）
        count = 0

        # 暴力做法：
        """
        for right in range(len(pfx_odd)):
            for left in range(right + 1):
                # 左闭右闭
                # pfx[-1] = 0
                pfx_l = pfx_odd[left - 1] if left > 0 else 0
                pfx_r = pfx_odd[right]
                if pfx_r ^ pfx_l:
                    count += 1
        """

        # 计数做法：
        count = [1, 0]  # 0 和 1 的个数
        # 注意 pfx[-1] = 0！预先加一个 0 进去
        odds = 0

        for right in range(len(pfx_odd)):
            pfx_r = pfx_odd[right]
            # 如果是 1，查找之前 0 的个数并加进去
            # 反之亦然
            odds += count[pfx_r ^ 1]
            count[pfx_r] += 1

        return odds % (10**9 + 7)


if __name__ == "__main__":
    assert Solution().numOfSubarrays([1, 3, 5]) == 4
