import requests

URL = 'https://api.api-ninjas.com/v1/animals?name='


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
    res = requests.get(new_url, headers={'X-Api-Key': 'UkkpAvnGuZ8I1p6h4hTfkA==b9sZdFDa2MqJyuyC'}).json()
    animals_html = animals_details(res)
    print(animals_html)


if __name__ == "__main__":
    main()
