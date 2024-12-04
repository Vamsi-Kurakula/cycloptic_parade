from crewai.tools.base_tool import BaseTool

class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Perform mathematical calculations, like addition, subtraction, multiplication, or division."

    def _run(self, expression: str) -> str:
        try:
            return str(eval(expression))
        except Exception as e:
            return f"Error: {str(e)}"