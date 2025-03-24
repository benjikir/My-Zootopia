import json

# Function to get all skin types available in the animal_data.json
def get_skin_types(data):
    """
    Extracts and returns a set of unique skin types from the animal data.

    Args:
        data (list): A list of animal dictionaries.

    Returns:
        set: A set of unique skin types.
    """
    skin_types = set()
    for animal in data:
        characteristics = animal.get('characteristics', {})
        skin_type = characteristics.get('skin_type')
        if skin_type:
            skin_types.add(skin_type)
    return skin_types

# Function to serialize a single animal object into HTML
def serialize_animal(animal_obj):
    """
    Serializes an animal object into an HTML list item.

    Args:
        animal_obj (dict): A dictionary containing animal data (name, diet, locations, type).

    Returns:
        str: An HTML string representing the animal as a list item.
    """
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {animal_obj["diet"]}<br/>\n'
    output += f'    <strong>Location:</strong> {", ".join(animal_obj["locations"])}<br/>\n'
    output += f'    <strong>Type:</strong> {animal_obj["type"]}<br/>\n'
    if 'skin_type' in animal_obj:
        output += f'    <strong>Skin Type:</strong> {animal_obj["skin_type"]}<br/>\n'  # Use skin_type if it exists
    output += '  </p>\n'
    output += '</li>\n'
    return output

# Function to generate animals HTML file from the template
def generate_html(data, template_file="animals_template.html", output_file="animals.html"):
    """
    Generates an HTML file containing animal data, using a template.

    Args:
        data (list): A list of animal dictionaries.
        template_file (str): The path to the HTML template file. Defaults to "animals_template.html".
        output_file (str): The path to the output HTML file. Defaults to "animals.html".
    """
    try:
        with open(template_file, 'r') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Error: Template file '{template_file}' not found.")
        return

    animals_html = ''
    for animal in data:
        name = animal.get('name')
        characteristics = animal.get('characteristics', {})
        diet = characteristics.get('diet')
        locations = animal.get('locations', [])
        animal_type = characteristics.get('type')
        skin_type = characteristics.get('skin_type')

        if all([name, diet, locations, animal_type]) and len(locations) > 0:
            animal_obj = {
                "name": name,
                "diet": diet,
                "locations": locations,
                "type": animal_type,

            }
            if skin_type:
                animal_obj["skin_type"] = skin_type #Correct assignment here!
            animals_html += serialize_animal(animal_obj)
        else:
            print(f"Skipping animal {name} due to missing data.")

    # Replace the placeholder in the template with the generated HTML
    output_html = template.replace('__REPLACE_ANIMALS_INFO__', f'<ul class="cards">\n{animals_html}\n</ul>')

    try:
        with open(output_file, 'w') as f:
            f.write(output_html)
        print(f"Successfully generated '{output_file}'.")
    except Exception as e:
        print(f"Error writing to file '{output_file}': {e}")


# Main execution block
if __name__ == "__main__":
    try:
        with open('animals_data.json', 'r') as file:
            animals_data = json.load(file)
    except FileNotFoundError:
        print("Error: 'animals_data.json' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'animals_data.json'.")
    else:
        # Example usage of the functions
        skin_types = get_skin_types(animals_data)
        print("Available skin types:", skin_types)  # Display available skin types

        generate_html(animals_data)