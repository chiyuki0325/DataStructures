class Solution:
    # 蛄蛹者
    def minWindow(self, s: str, t: str) -> str:
        # if len(t) > len(s):
        #    return ""

        result = ""
        left = 0
        right = -1

        # test = []
        # for i in range(ord("A"), ord("Z")+1):
        #    test.append(chr(i))
        # for i in range(ord("a"), ord("z")+1):
        #    test.append(chr(i))

        def print_freq(freq: list[int]):
            for i in range(len(freq)):
                if freq[i] != 0:
                    print(f"{test[i]}:{freq[i]} ", end="")
            print()

        def index(char: str) -> int:
            # 返回一个字符在freq数组中的索引
            o = ord(char)
            if o < 96:
                return o-65
            else:
                return o-71

        t_freq = [0]*52
        for char in t:
            t_freq[index(char)] += 1

        window_freq = [0]*52

        def check_window_freq() -> bool:
            nonlocal window_freq, t_freq
            for i in range(52):
                if t_freq[i] != 0:
                    if window_freq[i] < t_freq[i]:
                        return False
            return True

        def expand_right() -> bool:
            nonlocal right, window_freq
            _right = right
            _window_freq = window_freq.copy()
            while not check_window_freq():
                right += 1
                if right >= len(s):
                    right = _right
                    window_freq = _window_freq
                    # print("rollback", right, window_freq)
                    return False
                window_freq[index(s[right])] += 1

            # print("expand_right ends up with")
            # print(s[left:right+1])
            # print_freq(window_freq)
            # print()

            return True

        def shrink_left():
            nonlocal left, window_freq
            operated = False
            while check_window_freq():
                window_freq[index(s[left])] -= 1
                left += 1
                operated = True
            if operated:
                left -= 1
                window_freq[index(s[left])] += 1

            # print("shink_left ends up with")
            # print(s[left:right+1])
            # print_freq(window_freq)
            # print()

        def update_window():
            nonlocal left, right, result
            window = s[left:right+1]
            if len(result) == 0 or len(window) < len(result):
                result = window

        while right < len(s):
            exp = expand_right()
            if not expand_right():
                # print(left, right)
                update_window()
                return result
            shrink_left()

            update_window()

            # 强制蛄蛹一下
            right += 1
            if right < len(s):
                window_freq[index(s[right])] += 1
                window_freq[index(s[left])] -= 1
                left += 1

        # print(result)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "a") == "a"
    assert s.minWindow("a", "aa") == ""
    assert s.minWindow("a", "b") == ""
