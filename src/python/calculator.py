class Calculator:
    def add(self, a: int, b: int) -> int:
        result = a + b
        return result

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Cannot divide by " + str(b))
        return a / b