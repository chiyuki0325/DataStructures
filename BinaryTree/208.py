# 并非二叉树


class Node:
    def __init__(self, char: str | None = None):
        self.members = []
        self.char = char

    def get(self, char: str):
        for member in self.members:
            if member.char == char:
                return member
        return None

    def insert(self, char: str):
        new_node = Node(char)
        self.members.append(new_node)
        return new_node


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word + "\x00":
            member = cur.get(char)
            if member is None:
                member = cur.insert(char)
            cur = member

    def search(self, word: str) -> bool:
        return self.startsWith(word + "\x00")

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            member = cur.get(char)
            if member is None:
                return False
            cur = member
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
