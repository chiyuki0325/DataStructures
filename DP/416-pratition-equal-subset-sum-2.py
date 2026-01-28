class Solution:
    def canPartition2(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        total //= 2
        # 此时问题转变为：是否可以在 nums 中找出几个元素使其和等于 total？

        # 首先尝试暴力解法
        def dfs(_nums, _total) -> bool:
            if _total == 0:
                return True
            if _total < 0:
                return False
            return any(
                dfs(_nums[:i] + _nums[i + 1 :], _total - _nums[i])
                for i in range(len(_nums))
            )

        # @cache 不能加，Unhashable type 'list'
        # 有个邪道：用一个二进制数字表示 nums 中还存在的项目
        # 显然不是正解
        return dfs(nums, total)

        # 这种方法错在把「选或不选」问题想成了「枚举选哪个」问题
        # 所以让我们直接重来


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        total //= 2

        n = len(nums)

        # 选或不选
        @cache
        def dfs(i, _total) -> bool:
            if _total == 0:
                return True
            if _total < 0 or i == n:
                return False
            return dfs(i + 1, _total) or dfs(i + 1, _total - nums[i])

        return dfs(0, total)


s = Solution().canPartition
assert s([1, 5, 11, 5]) == True
assert s([1, 2, 3, 5]) == False
assert s([1, 2, 5]) == False
