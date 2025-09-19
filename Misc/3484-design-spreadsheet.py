from typing import Optional


class Spreadsheet:
    def list26(self):
        return [0] * 26

    def __init__(self, rows: int):
        # 初始化
        self.sheet = []
        for i in range(rows):
            self.sheet.append(self.list26())
        # A2: self.sheet[1][0]

    def cell_to_index(self, cell: str) -> Optional[tuple[int, int]]:
        if cell[0].isupper() and cell[1:].isnumeric():
            # 是格子编号
            return (int(cell[1:])-1, ord(cell[0])-65)
        else:
            # 是字面量
            return None

    def setCell(self, cell: str, value: int) -> None:
        x, y = self.cell_to_index(cell)
        self.sheet[x][y] = value

    def resetCell(self, cell: str) -> None:
        # 重置0
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        # 把表达式切割为前后两部分
        formula_list = []
        cache = ""
        for char in formula[1:]:
            if char == "+":
                formula_list.append(cache)
                cache = ""
            else:
                cache += char
        formula_list.append(cache)

        nums = []
        for unit in formula_list:
            index = self.cell_to_index(unit)
            if index:
                x, y = index
                nums.append(self.sheet[x][y])
            else:
                nums.append(int(unit))

        return sum(nums)


if __name__ == "__main__":
    s: Optional[Spreadsheet] = None
    null = None
    cases = ["Spreadsheet", "getValue", "setCell", "getValue",
             "setCell", "getValue", "resetCell", "getValue"]
    args = [[3], ["=5+7"], ["A1", 10], ["=A1+6"],
            ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]
    results = [null, 12, null, 16, null, 25, null, 15]

    for i in range(len(cases)):
        c = cases[i]
        match c:
            case "Spreadsheet":
                s = Spreadsheet(args[i][0])
            case "getValue":
                assert s.getValue(args[i][0]) == results[i]
            case "setCell":
                s.setCell(args[i][0], args[i][1])
            case "resetCell":
                s.resetCell(args[i][0])
