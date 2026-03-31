namespace DemoApp;

/// <summary>
/// A simple calculator class with intentional bugs
/// that will cause the GitHub Actions build to fail.
/// The self-healing agent should detect and fix these.
/// </summary>
public class Calculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }

    public int Subtract(int a, int b)
    {
        return a - b;   // Fixed: added missing semicolon
    }

    public int Multiply(int a, int b)
    {
        return a * b;
    }

    // Fixed: return type changed from string to double
    public double Divide(int a, int b)
    {
        if (b == 0)
            throw new DivideByZeroException("Cannot divide by zero");
        return (double)a / b;
    }
}