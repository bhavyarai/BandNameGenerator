# This code will generate a band name for you

def generate_band_name(city, pet):
    return f"{city} {pet}"


if __name__ == '__main__':
    city = input("The city you were born in: ")
    pet = input("Your pet name: ")
    band = generate_band_name(city, pet)
    print(f"Your band name should be {band}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
