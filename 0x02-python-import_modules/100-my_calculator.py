#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    def handle_operation(a, operator, b):
        if operator == "+":
            result = add(a, b)
            op_symb = "+"
        elif operator == "*":
            result = mul(a, b)
            op_symb = "*"
        elif operator == "/":
            result = div(a, b)
            op_symb = "/"
        elif operator == "-":
            result = sub(a, b)
            op_symb = "-"
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(a, op_symb, b, result))

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    handle_operation(a, operator, b)
