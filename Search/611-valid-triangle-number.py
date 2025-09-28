from typing import List


class Solution:
    # 自己写出来的吊车尾写法，五千多毫秒，但是能过
    # 最坏时间复杂度 O(n^2 logn)
    # 但加上缓存，一般到不了这个操作数量
    def triangleNumber(self, nums: List[int]) -> int:
        def find_index3(index2: int, sum12: int) -> int:
            l = index2
            r = len(nums)-1
            candidate = None
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < sum12:
                    candidate = mid
                    l = mid+1
                else:
                    r = mid-1
            return candidate

        if len(nums) < 3:
            return 0
        nums.sort()
        # print(nums)
        count = 0
        for index1 in range(len(nums)):
            # 缓存计算结果，跳过重复元素
            last_index2 = None
            last_count_add=None
            for index2 in range(index1+1, len(nums)):
                # 检查缓存
                if index2 == last_index2:
                    if last_count_add:
                        count+=last_count_add
                        continue
                sum12 = nums[index1] + nums[index2]
                index3 = find_index3(index2, sum12)
                last_index2 = index2
                last_count_add = None
                if index3 and index3 > index2:
                    # print(nums[index1], nums[index2], nums[index3])
                    last_count_add = index3-index2
                    count+=last_count_add
        # print(count)
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.triangleNumber([2, 2, 3, 4]) == 3
    assert s.triangleNumber([4, 2, 3, 4]) == 4
