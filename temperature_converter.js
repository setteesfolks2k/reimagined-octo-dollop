function celsiusToFahrenheit(celsius) {
    return (celsius * 9/5) + 32;
}

function fahrenheitToCelsius(fahrenheit) {
    return (fahrenheit - 32) * 5/9;
}

let temp = 100;
console.log(`🌡️ ${temp}°C = ${celsiusToFahrenheit(temp)}°F`);
console.log(`🌡️ ${temp}°F = ${fahrenheitToCelsius(temp)}°C`);
