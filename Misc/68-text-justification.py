from typing import List

class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        # 不是，这玩意是困难？
        output = []
        n = len(words)

        prep_idx = 0
        while prep_idx < n:
            start_word_idx = prep_idx
            line_words = 0
            line_len = -1  # 反正最后要减去一个多余的空格，不如初始化为 -1
            left_justify = False

            while True:
                line_len += len(words[prep_idx]) + 1
                prep_idx += 1
                line_words += 1
                if line_len > max_width:
                    # 去除一个多余的单词
                    prep_idx -= 1
                    line_words -= 1
                    line_len -= (len(words[prep_idx]) + 1)
                    break
                if prep_idx == n:
                    left_justify = True
                    break

            remaining_spaces = max_width - line_len  # 剩余可供分配的空格数

            if left_justify:
                each_word_spaces = 1
                extra_space_words = 0
            else:
                if line_words > 1:
                    each_word_spaces = remaining_spaces // (line_words - 1) + 1  # 每个单词之间的空格数
                    extra_space_words = remaining_spaces % (line_words - 1)  # 多出的空格
                else:
                    each_word_spaces = remaining_spaces
                    extra_space_words = 0

            # 把此行的单词上屏
            line = ""
            for i in range(line_words):
                enter_idx = start_word_idx + i
                line += words[enter_idx]
                line += " " * each_word_spaces
                if i < extra_space_words:
                    line += " "
            if line_words > 1:
                line = line[:-each_word_spaces]
            if left_justify:
                line += " " * (max_width - len(line))
            # print(line, len(line))
            # assert len(line) == max_width
            # ???
            if len(line) > max_width:
                line = line[:max_width]
            output.append(line)

        return output

if __name__=="__main__":
    print(Solution().fullJustify(['a'],1))
    print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"],16))
    print(Solution().fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16))
