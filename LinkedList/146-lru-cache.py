class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def pickaway(self, node: Node):
        # 从链表中摘出
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def append(self, node: Node):
        # 放到链表头部
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def floatup(self, node: Node):
        # 浮到队首
        self.pickaway(node)
        self.append(node)
        return node

    def sinktail(self):
        # 队尾的元素沉底
        return self.pickaway(self.tail.prev)


class LRUCache:
    def __init__(self, capacity: int):
        self.deque = Deque()  # 存储数据
        self.pointers = {}  # key->Node*
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.pointers:
            return -1
        # 存在
        node = self.pointers[key]
        self.deque.floatup(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.pointers:
            # 新建
            node = Node(key, value)
            self.pointers[key] = node
            self.deque.append(node)
            self.size += 1
            if self.size > self.capacity:
                # 容量满了
                sinked = self.deque.sinktail()
                self.pointers.pop(sinked.key)  # 删除指针
                self.size -= 1
        else:
            # 更新
            node = self.pointers[key]
            node.val = value
            self.deque.floatup(node)
