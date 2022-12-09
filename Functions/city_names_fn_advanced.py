def city_country(city, country):
    city_name = f"{city}, {country}"
    return city_name

while True:
    print(f"\nPlease Enter the names of City&Country.")
    print(f"\nPlease enter 'q' to close any time.")
    city_n = input("\nName of the City:\t")
    if city_n == 'q':
        break
    country_n = input("\nName of the Country:\t")
    if country_n == 'q':
        break

    names = city_country(city_n, country_n)
    print(names)