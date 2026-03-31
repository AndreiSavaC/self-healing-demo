using DemoApp;

var calc = new Calculator();

Console.WriteLine("=== Calculator ===");
Console.WriteLine($"2 + 3 = {calc.Add(2, 3)}");
Console.WriteLine($"10 - 4 = {calc.Subtract(10, 4)}");
Console.WriteLine($"5 * 6 = {calc.Multiply(5, 6)}");
Console.WriteLine($"15 / 3 = {calc.Divide(15, 3)}");
Console.WriteLine($"2^10 = {calc.Power(2, 10)}");
Console.WriteLine($"sqrt(144) = {calc.Sqrt(144)}");
Console.WriteLine($"5! = {calc.Factorial(5)}");
Console.WriteLine($"10 % 3 = {calc.Modulo(10, 3)}");

Console.WriteLine("\n=== Converter ===");
Console.WriteLine($"0°C = {UnitConverter.CelsiusToFahrenheit(0)}°F");
Console.WriteLine($"98.6°F = {UnitConverter.FahrenheitToCelsius(98.6)}°C");
Console.WriteLine($"42.195 km = {UnitConverter.KmToMiles(42.195)} miles");
Console.WriteLine($"1 kg = {UnitConverter.KgToPounds(1)} lbs");

