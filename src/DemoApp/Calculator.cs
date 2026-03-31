namespace DemoApp;

/// <summary>
/// Calculator with basic and advanced operations.
/// </summary>
public class Calculator
{
    public int Add(int a, int b) => a + b;

    public int Subtract(int a, int b)
    {
        return a - b;
    }

    public int Multiply(int a, int b) => a * b;

    public double Divide(int a, int b)
    {
        if (b == 0)
            throw new DivideByZeroException("Cannot divide by zero");
        return (double)a / b;
    }

    public double Power(double baseVal, double exponent) => Math.Pow(baseVal, exponent);

    public double Sqrt(double value)
    {
        if (value < 0)
            throw new ArgumentException("Cannot take square root of a negative number");
        return Math.Sqrt(value);
    }

    /// <summary>
    /// Calculate factorial of n. 
    /// BUG: Uses int instead of long — overflows silently for n > 12
    /// because int.MaxValue is only 2,147,483,647 but 13! = 6,227,020,800
    /// </summary>
    public int Factorial(int n)
    {
        if (n < 0) throw new ArgumentException("Factorial not defined for negative numbers");
        if (n <= 1) return 1;

        int result = 1;
        for (int i = 2; i <= n; i++)
        {
            // BUG: unchecked int overflow for n >= 13
            result *= i;
        }
        return result;
    }

    public int Modulo(int a, int b)
    {
        if (b == 0)
            throw new DivideByZeroException("Cannot modulo by zero");
        return a % b;
    }

    public int Abs(int value) => Math.Abs(value);

    public int Negate(int value) => -value;
}

