import json

# Function to serialize a single animal object into HTML
def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {animal_obj["diet"]}<br/>\n'
    output += f'    <strong>Location:</strong> {", ".join(animal_obj["locations"])}<br/>\n'
    output += f'    <strong>Type:</strong> {animal_obj["type"]}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output

# Open the JSON file and load the data
with open('animals_data.json', 'r') as file:
    data = json.load(file)

# Initialize the HTML structure
output = '<ul class="cards">\n'

# Iterate through the data and serialize each animal
for animal in data:
    name = animal.get('name')
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet')
    locations = animal.get('locations', [])
    animal_type = characteristics.get('type')

    # Ensure all required data exists
    if all([name, diet, locations, animal_type]) and len(locations) > 0:
        # Prepare the animal data to pass to the serializer
        animal_obj = {
            "name": name,
            "diet": diet,
            "locations": locations,
            "type": animal_type
        }
        # Serialize the animal and append it to the output
        output += serialize_animal(animal_obj)
    else:
        print(f"Skipping animal {name} due to missing data.")

# Close the list tag and print the final HTML
output += '</ul>\n'

# Optionally, save the result to an HTML file
with open('animals_output.html', 'w') as html_file:
    html_file.write(output)

# Print the HTML output to the console
print(output)
