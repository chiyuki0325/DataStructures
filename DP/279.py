class Solution:
    def numSquares(self, n: int) -> int:
        counts=[0]*(n+1)
        for i in range(1,n+1):
            count=10001 #数据范围
            j=1
            while  j*j<=i:
                count=min(count,counts[i-j*j]+1)
                j+=1
            counts[i]=count
        return counts[n]

