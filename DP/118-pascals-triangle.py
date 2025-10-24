class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # 经典递推法，经典得不能再经典了
        triangle = [[1]]

        # 1
        # 1 1
        # 1 2 1
        # 1 3 3 1
        # 1 4 6 4 1

        for line_idx in range(1, numRows):
            line_len = line_idx + 1
            triangle.append([1] * line_len)

            # 根据上一行的值，推出下一行每个格子的值
            last_line = triangle[line_idx - 1]
            this_line = triangle[line_idx]
            for i in range(line_idx - 1):
                this_line[i + 1] = last_line[i] + last_line[i + 1]

        return triangle


if __name__ == "__main__":
    print(Solution().generate(5))
