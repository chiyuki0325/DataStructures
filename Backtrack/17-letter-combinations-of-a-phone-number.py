class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        end = len(digits)
        result = []
        chars = ["", "", "abc", "def", "ghi",
                 "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def recur(path: str, depth: int):
            if depth == end:
                return result.append(path)
            for char in chars[int(digits[depth])]:
                recur(path+char, depth+1)

        recur("", 0)
        return result


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
