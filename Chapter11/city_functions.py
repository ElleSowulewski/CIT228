def city_string(city, country, population = ""):
    if population != "":
        string = (f"{city}, {country} = population {population}")
    else:
        string = (f"{city}, {country}")
    return string