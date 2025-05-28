class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # O(log(n))
        r = len(arr)-1
        l = 0

        def search(arr: List[int], l: int, r: int) -> int:
            i = (l+r)//2
            i1, i2, i3 = i-1, i, i+1

            if i>0:
                if arr[i1]<arr[i2]<arr[i3]:
                    # i在左半部分
                    return search(arr, i, r)
                elif arr[i1]>arr[i2]>arr[i3]:
                    # i在右半部分
                    return search(arr, l, i)
                else:
                    return i
            else:
                #i为0
                return 0

        return search(arr,l, r)
