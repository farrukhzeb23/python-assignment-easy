
units = ("celsius", "fahrenheit")


def temperature_converter(temperature, unit):
    converters = {
        'celsius': lambda temp: (temp * 9/5) + 32,
        'fahrenheit': lambda temp: (temp - 32) * 5/9
    }
    handlers = converters.get(unit)
    return handlers(temp=temperature)


def get_temperature_input():
    while True:
        try:
            temp = input("Enter the temperature: ")
            return float(temp)
        except ValueError:
            print("Please enter a valid temperature number.")


def get_unit_input():
    while True:
        unit = input("Enter the unit (Celsius/Fahrenheit): ").lower()
        if unit in units:
            return unit
        else:
            print("Please enter 'Celsius' or 'Fahrenheit'.")


temp = get_temperature_input()
unit = get_unit_input()
converted = temperature_converter(temp, unit)
print(f"{converted} {unit.capitalize()}")
