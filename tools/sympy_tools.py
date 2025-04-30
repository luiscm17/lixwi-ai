from sympy import symbols, Eq, solve
from sympy.parsing.sympy_parser import parse_expr

def solve_expression(expr: str):
    x = symbols('x')
    if '=' in expr:
        left, right = expr.split('=')
        equation = Eq(parse_expr(left), parse_expr(right))
        solution = solve(equation, x)
    else:
        solution = solve(parse_expr(expr), x)
    return solution
