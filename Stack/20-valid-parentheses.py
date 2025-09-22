class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        lefts = ['(', '[', '{']
        rights = [')', ']', '}']
        rtl = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in lefts:
                brackets.append(c)
            elif c in rights:
                if len(brackets) == 0:
                    return False
                if brackets[-1] != rtl[c]:
                    return False
                else:
                    brackets.pop()
            else:
                return False
        return len(brackets) == 0
