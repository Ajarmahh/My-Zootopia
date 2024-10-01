# My-Zootopia

My-Zootopia is a Python project that fetches animal data from the [Ninja API](https://api-ninjas.com/api/animals) and generates an HTML file with information about the animal. 
The app uses the `requests` library to make HTTP requests and the `python-dotenv` library to manage API keys through environment variables.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [How it Works](#how-it-works)
- 

## Installation

### Prerequisites

- Python 3.x installed on your machine.
- `pip` (Python package manager).
- An API key from [Ninja API](https://api-ninjas.com/register).

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Ajarmahh/My-Zootopia.git
   cd My-Zootopia

2. Install the required dependencies:
  - pip install -r requirements.txt

3. Create a .env file in the root of your project directory and add your API key


### Usage

1. Run the Python script

2. Enter the name of the animal 

3. The program will fetch the animal data from the API, generate an HTML file named animals.html, and populate it with information about the animal

4. Open the animals.html file in your web browser to see the generated webpage


### Project Structure

.
├── data_fetcher.py          # Handles API requests and checks if the animal exists
├── main_script.py           # Main logic to generate the HTML file
├── animals_template.html    # HTML template with a placeholder for animal data
├── .env                     # Environment variables (API key)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


### Environment Variables

This project uses a .env file to manage the API key securely. You'll need to create a .env file with the following content


### How it Works

1. The user is prompted to input an animal's name
2. The script fetches the animal data using the requests library and Ninja API
3. If the animal exists, it generates an HTML file (animals.html) by replacing a placeholder in the animals_template.html with real data
4. If the animal does not exist, a message is generated informing the user that the animal doesn't exist
5. The final HTML file is created and can be viewed in a web browser


