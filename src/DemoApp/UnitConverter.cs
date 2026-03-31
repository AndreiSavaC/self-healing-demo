namespace DemoApp;

/// <summary>
/// Unit converter matching the Python converter module.
/// FIXED: Corrected Fahrenheit-to-Celsius formula with proper parentheses.
/// Was: f - 32 * 5.0 / 9.0 → Evaluates as f - 17.78 (incorrect)
/// Now: (f - 32) * 5.0 / 9.0 → Correctly computes temperature conversion
/// </summary>
public class UnitConverter
{
    public static double CelsiusToFahrenheit(double c) => (c * 9.0 / 5.0) + 32.0;

    // FIXED: Added parentheses around (f - 32) to ensure correct operator precedence
    public static double FahrenheitToCelsius(double f) => (f - 32) * 5.0 / 9.0;

    public static double CelsiusToKelvin(double c)
    {
        var result = c + 273.15;
        if (result < 0)
            throw new ArgumentException($"Temperature below absolute zero: {result}K");
        return result;
    }

    public static double KmToMiles(double km)
    {
        if (km < 0) throw new ArgumentException("Distance cannot be negative");
        return km * 0.621371;
    }

    public static double MilesToKm(double miles)
    {
        if (miles < 0) throw new ArgumentException("Distance cannot be negative");
        return miles * 1.60934;
    }

    public static double KgToPounds(double kg)
    {
        if (kg < 0) throw new ArgumentException("Weight cannot be negative");
        return kg * 2.20462;
    }

    public static double PoundsToKg(double lbs)
    {
        if (lbs < 0) throw new ArgumentException("Weight cannot be negative");
        return lbs * 0.453592;
    }
}