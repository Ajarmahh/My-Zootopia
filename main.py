import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def animals_details(data):
    output = ""
    for animal in data:
        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        location = animal["locations"][0]
        animal_type = animal["characteristics"].get("type", "-")  # Check if type exists and set animal_type accordingly

        # Generate the list item HTML
        output += f'''
                        <ul class="cards">
                            <li class="cards__item">
                                <div class="card__title">{name}</div>
                                <p class="card__text">
                                   <strong>Diet:</strong> {diet} <br/>
                                  <strong>Location:</strong> {location} <br/>
                                  <strong>Type:</strong> {animal_type} <br/>
                                </p>
                            </li> 
                        </ul>
                        '''
    return output


def main():
    animals_data = load_data('animals_data.json')
    animals_html = animals_details(animals_data)

    with open('animals_template.html', 'r') as f:
        html_data = f.read()

    final_html_data = html_data.replace('__REPLACE_ANIMALS_INFO__', animals_html)

    with open('animals.html', 'w') as f:
        f.write(final_html_data)


if __name__ == "__main__":
    main()
