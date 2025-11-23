## create dictionaries using an expression with for loops and lambda

#example dictionary

cities_F = {"Budapest": 23, "London": 45, "Bonn": 56, "Bergen": 21}

#converting temps to C

cities_C = {key: round((value-32) * (5 / 9)) for (key,value) in cities_F.items()}

print(cities_C)

#different example

weather = {"Budapest": "Sunny", "London": "Rainy", "Bonn": "Cloudy", "Bergen": "Cloudy", "Rome": "Sunny"}

weather_sunny = {key: value for (key,value) in weather.items() if value == "Sunny"}
print(weather_sunny)

#third example replacing the temp values with text

cities_F = {"Budapest": 23, "London": 45, "Bonn": 56, "Bergen": 21}

cities_textTemp = {key: ("warm" if value >= 40 else "cold")  for (key,value) in cities_F.items()}
print(cities_textTemp)

#using function in the code
def check_temp(value):
    if value > 70: 
        return "hot"
    elif 69 >= value >= 40:
        return "warm"
    else: 
        return "cold"
 
cities_F = {"Budapest": 23, "London": 45, "Bonn": 56, "Bergen": 21, "Heraklion": 89}
cities_text_withFunction = {key: check_temp(value) for (key,value) in cities_F.items()}
print(cities_text_withFunction)

