from data_fetcher import fetch_animal_data, is_animal_exist


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
    name = input('Type animal name: ')
    animal_data = fetch_animal_data(name)

    """
          the animals API returns an empty list in case the user entered a non-existing animal
          and the if Statement will check if the API returned an empty list
       """
    if not is_animal_exist(animal_data):
        animals_html = f"<h2>The animal '{name}' doesn't exist.</h2>"
    else:
        animals_html = animals_details(animal_data)

    with open('animals_template.html', 'r') as f:
        html_data = f.read()

    final_html_data = html_data.replace('__REPLACE_ANIMALS_INFO__', animals_html)

    with open('animals.html', 'w') as f:
        f.write(final_html_data)
    print('Website was successfully generated to the file animals.html.')


if __name__ == "__main__":
    main()