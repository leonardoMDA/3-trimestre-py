def celsius_para_fahrenheit(celsius):

  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

temperatura_celsius = 30
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C equivalem a {temperatura_fahrenheit}°F")