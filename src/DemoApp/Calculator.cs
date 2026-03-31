// ┌─────────────────────────────────────────────────────────────────┐
// │  DEMO: This file contains INTENTIONAL BUGS for the             │
// │  self-healing agent to detect and fix.                         │
// │                                                                 │
// │  Bug 1: Missing semicolon on line 26 → Build failure           │
// │  Bug 2: Wrong return type on Divide method → Build failure     │
// └─────────────────────────────────────────────────────────────────┘

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
        return a - b   // BUG: Missing semicolon → CS1002 error
    }

    public int Multiply(int a, int b)
    {
        return a * b;
    }

    // BUG: Return type is 'string' but should be 'double' → CS0029 error
    public string Divide(int a, int b)
    {
        if (b == 0)
            throw new DivideByZeroException("Cannot divide by zero");
        return (double)a / b;
    }
}
