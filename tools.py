import json
import ast
import operator

with open("orders.json", "r") as f:
    ORDERS = json.load(f)

def lookup_order(order_id):
    if order_id not in ORDERS:
        return {"error": f"Order {order_id} not found"}

    return ORDERS[order_id]

def calculate(expression):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
    }

    def eval_node(node):
        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):
            return operators[type(node.op)](
                eval_node(node.left),
                eval_node(node.right)
            )

        if isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](
                eval_node(node.operand)
            )

        raise ValueError("Unsupported expression")

    tree = ast.parse(expression, mode="eval")
    return eval_node(tree.body)