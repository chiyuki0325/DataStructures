def quicksort(nums: list[int]):
    def helper(left: int, right: int):
        if left >= right:
            return
        pivot = partition(left, right)
        hepler(left, pivot-1)
        helper(pivot+1, right)

    def partition(left: int, right: int) -> int:
        # 返回 pivot 的索引
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1
            while i < j and nums[i] <= nums[left]:
                i += 1
            # i 是最左边的大于元素，j 是最右边的小于元素
            nums[i], nums[j] = nums[j], nums[i]
        # 划分已经完成
        # 把 pivot 移到分界线处（i）
        nums[i], nums[left] = nums[left], nums[i]
        return i

    helper(nums, 0, len(nums)-1)
