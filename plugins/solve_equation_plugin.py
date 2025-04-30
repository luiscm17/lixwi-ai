from semantic_kernel.functions import kernel_function
from typing import Annotated
from tools.sympy_tools import solve_expression

class SolveEquationPlugin:
    """Plugin que resuelve ecuaciones simbólicas con SymPy"""

    @kernel_function(
        description="Resuelve una ecuación simbólica matemática",
    )
    def solve_equation(self, input: Annotated[str, "Ecuación como string"]) -> str:
        try:
            result = solve_expression(input)
            return f"La solución es: {result}"
        except Exception as e:
            return f"No se pudo resolver la ecuación: {e}"
