import requests

URL = 'https://api.api-ninjas.com/v1/animals?name='
API_KEY = 'UkkpAvnGuZ8I1p6h4hTfkA==b9sZdFDa2MqJyuyC'


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
    name = input('type animal name: ')
    new_url = f'{URL}{name}'
    res = requests.get(new_url, headers={'X-Api-Key': API_KEY}).json()

    """
       the animals API returns an empty list in case the user entered a non-existing animal
       and the if Statement will check if the API returned an empty list
    """
    if not res:
        animals_html = f"<h2>The animal '{name}' doesn't exist.</h2>"
    else:
        animals_html = animals_details(res)

    with open('animals_template.html', 'r') as f:
        html_data = f.read()

    final_html_data = html_data.replace('__REPLACE_ANIMALS_INFO__', animals_html)

    with open('animals.html', 'w') as f:
        f.write(final_html_data)
    print('Website was successfully generated to the file animals.html.')


if __name__ == "__main__":
    main()
