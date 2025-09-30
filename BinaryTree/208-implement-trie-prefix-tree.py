from typing import Optional, List

class TreeNode:
    def __init__(self):
        self.is_end = False
        self.children: List[Optional['TreeNode']] = [None]*26


class Trie:
    def __init__(self):
        self.root: TreeNode = TreeNode()

    def _ord(self, char: str) -> int:
        return ord(char)-97

    def insert(self, word: str) -> None:
        cur: Optional[TreeNode] = self.root

        for char in word:
            pos = self._ord(char)
            if cur.children[pos] is None:
                cur.children[pos] = TreeNode()
            cur = cur.children[pos]

        cur.is_end = True

    def search(self, word: str) -> bool:
        cur: Optional[TreeNode] = self.root

        for char in word:
            pos = self._ord(char)
            if cur.children[pos] is None:
                return False
            cur = cur.children[pos]

        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur: Optional[TreeNode] = self.root

        for char in prefix:
            pos = self._ord(char)
            if cur.children[pos] is None:
                return False
            cur = cur.children[pos]

        return True
