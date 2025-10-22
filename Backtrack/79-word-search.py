from typing import List


class Solution:
    # 查看题解后修复神秘撞尾 bug
    # “恢复现场”入门

    def exist(self, board: List[List[str]], word: str) -> bool:
        border_y, border_x = len(board), len(board[0])

        def check(y: int, x: int, pos: int):
            return 0 <= y < border_y and 0 <= x < border_x and pos < len(word) and board[y][x] == word[pos]

        def dfs(y: int, x: int, pos: int) -> bool:
            if pos == len(word):
                return True

            if not check(y, x, pos):
                return False

            # 一路找字母一路把 board[y][x] 标记为已访问，防止撞尾
            board[y][x] = ''
            new_pos = pos+1

            if dfs(y+1, x, new_pos) or dfs(y-1, x, new_pos) or dfs(y, x+1, new_pos) or dfs(y, x-1, new_pos):
                return True
            else:
                # “恢复现场”
                board[y][x] = word[pos]
                return False

        # 第一步：暴力查找单词的第一个字母
        for head_y in range(border_y):
            for head_x in range(border_x):
                # 第二步：DFS 递归查找单词的剩余字母

                if dfs(head_y, head_x, 0):
                    return True

        return False


if __name__ == "__main__":
    print(Solution().exist([["A", "B", "C", "E"], [
          "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
