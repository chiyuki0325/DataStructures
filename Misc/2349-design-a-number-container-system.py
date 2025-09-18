import heapq


class NumberContainers:
    def __init__(self):
        self.nc: dict[int, list] = {}  # number -> heap[index]
        self.nc_dict: dict[int, int] = {}  # index -> number

    def change(self, index: int, number: int) -> None:
        if number in self.nc:
            heapq.heappush(self.nc[number], index)
        else:
            self.nc[number] = [index]
        self.nc_dict[index] = number

    def find(self, number: int) -> int:
        if number in self.nc:
            heap = self.nc[number]
            # 延迟清理
            while len(heap) > 0 and self.nc_dict[heap[0]] != number:
                heapq.heappop(heap)
            if len(heap) == 0:
                return -1
            else:
                return heap[0]
        else:
            return -1


if __name__ == "__main__":
    tc = [
        "NumberContainers",
        "change",
        "find",
        "find",
        "find",
        "change",
        "change",
        "change",
        "change",
        "change",
        "change",
        "change",
        "change",
        "change",
        "find",
        "change",
        "find",
        "find",
        "change",
        "find",
        "change",
    ]
    args = [
        [],
        [75, 40],
        [14],
        [41],
        [40],
        [27, 40],
        [22, 14],
        [85, 14],
        [22, 40],
        [18, 34],
        [92, 41],
        [22, 40],
        [75, 40],
        [59, 34],
        [40],
        [27, 14],
        [34],
        [14],
        [13, 34],
        [40],
        [18, 41],
    ]
    null = None
    resp = [
        null,
        null,
        -1,
        -1,
        75,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        22,
        null,
        18,
        27,
        null,
        22,
        null,
    ]
    nc = NumberContainers()
    for i in range(len(tc)):
        print(tc[i], args[i])
        match tc[i]:
            case "find":
                assert nc.find(args[i][0]) == resp[i]
                print(resp[i])
            case "change":
                nc.change(args[i][0], args[i][1])
        print(nc.nc)
        print(nc.nc_dict)
