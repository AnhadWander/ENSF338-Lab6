import sys

def infix_to_postfix(tokens):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    output = []
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return output

def parse_postfix(postfix):
    stack = []
    for token in postfix:
        if token in {"+", "-", "*", "/"}:
            right = stack.pop()
            left = stack.pop()
            node = {"value": token, "left": left, "right": right}
            stack.append(node)
        else:
            stack.append({"value": int(token), "left": None, "right": None})
    return stack[0]

def evaluate_tree(node):
    if node["left"] is None and node["right"] is None:
        return node["value"]
    left_value = evaluate_tree(node["left"])
    right_value = evaluate_tree(node["right"])
    if node["value"] == "+":
        return left_value + right_value
    elif node["value"] == "-":
        return left_value - right_value
    elif node["value"] == "*":
        return left_value * right_value
    elif node["value"] == "/":
        return int(left_value / right_value)
    else:
        raise ValueError(f"Unknown operator: {node['value']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex3.py <expression>")
        sys.exit(1)

    expression = sys.argv[1]

    tokens = expression.split()

    try:
        postfix = infix_to_postfix(tokens)
    except Exception as e:
        print(f"Error converting to postfix: {e}")
        sys.exit(1)

    try:
        tree = parse_postfix(postfix)
    except Exception as e:
        print(f"Error parsing expression: {e}")
        sys.exit(1)

    try:
        result = evaluate_tree(tree)
        print(result)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        sys.exit(1)