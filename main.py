import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def animals_details(data):
    for animal in data:
        if 'type' not in animal['characteristics']:
            pass
        else:
            name = animal["name"]
            diet = animal["characteristics"]["diet"]
            location = animal["locations"][0]
            animal_type = animal["characteristics"]["type"]

            print(f'Name: {name}\nDiet: {diet}\nLocation: {location}\nType: {animal_type}\n')


animals_details(animals_data)