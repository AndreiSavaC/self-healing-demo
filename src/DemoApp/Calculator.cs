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
    /// FIXED: Changed return type from int to long to prevent overflow for n >= 13
    /// int.MaxValue is 2,147,483,647, but 13! = 6,227,020,800
    /// </summary>
    public long Factorial(int n)
    {
        if (n < 0) throw new ArgumentException("Factorial not defined for negative numbers");
        if (n <= 1) return 1;

        long result = 1;
        for (int i = 2; i <= n; i++)
        {
            // Fixed: Use long to prevent overflow for n >= 13
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

