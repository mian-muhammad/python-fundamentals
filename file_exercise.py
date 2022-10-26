import json

def main():
    # cities_file = open("cities.json")
    # cities_data = json.load(cities_file)
    # print(cities_data)

    # print("Largest cities in the US by population")

    # for index, entry in enumerate(cities_data):
    #     print(f"{index + 1}: {entry['name']} - {entry['pop']}")

    # with open("cities.json") as cities_file:
    #     cities_data = json.load(cities_file)

    #     print("Largest cities in the US by population")

    #     for index, entry in enumerate(cities_data):
    #         print(f"{index + 1}: {entry['name']} - {entry['pop']}")

    with open("cities.json") as cities_file:
        try:
            cities_data = json.load(cities_file)


            print("Largest cities in the US by population")
            for index, entry in enumerate(cities_data):
                print(f"{index + 1}: {entry['name']} - {entry['pop']}")

        except json.decoder.JSONDecodeError as error:
            print("Sorry, there was an error decoding that json file:")
            print(f"\t {error}")

if __name__ == "__main__":
    main()
