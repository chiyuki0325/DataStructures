def calculator(expr: str):
    cursor = 0
    nums = []
    operators = []

    # 运算符优先级
    precedence = {
        '+': 1, '-': 1,
        '*': 2, '/': 2,
        '(': 0
    }

    def read_number():
        # 读取一个数，并压入 nums 栈
        nonlocal expr
        nonlocal cursor
        num = 0

        while cursor < len(expr) and expr[cursor].isdigit():
            num = num * 10 + (ord(expr[cursor]) - 48)
            cursor += 1

        if cursor < len(expr) and expr[cursor] == '.':
            # 进入小数点模式
            cursor += 1
            after_decimal = 1
            while cursor < len(expr) and expr[cursor].isdigit():
                num += (ord(expr[cursor]) - 48) / (10 * after_decimal)
                cursor += 1
                after_decimal += 1

        nums.append(num)

    def calculate(a, b, op):
        # 进行一次运算
        match op:
            case '+':
                return a+b
            case '-':
                return a-b
            case '*':
                return a*b
            case '/':
                return a/b
            case _:
                raise SyntaxError()

    def calculate_single():
        # 进行单次计算
        a = nums.pop()
        b = nums.pop()
        op = operators.pop()
        # print(f"{b} {op} {a}")
        nums.append(calculate(a, b, op))

    def calculate_subexpr():
        # 进行计算，直到当前子表达式弹出完毕
        # 并把运算结果压入 nums
        while operators and operators[-1] != '(':
            calculate_single()
        if operators and operators[-1] == '(':
            operators.pop()

    # 主循环
    while cursor < len(expr):
        char = expr[cursor]

        if char == ' ':
            cursor += 1
        elif char.isdigit():
            read_number()
        elif char == '(':
            operators.append(char)
            cursor += 1
        elif char == ')':
            calculate_subexpr()
            cursor += 1
        elif char in ['+', '-', '*', '/']:
            while (operators and
                   precedence[operators[-1]] >= precedence[char]):
                # 计算优先级较高的运算符（先乘除后加减）
                calculate_single()
            operators.append(char)
            cursor += 1
        else:
            raise SyntaxError()

    calculate_subexpr()
    return nums.pop()


if __name__ == "__main__":
    while True:
        print(calculator(input("Expression: ")))
