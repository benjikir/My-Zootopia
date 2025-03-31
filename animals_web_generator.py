import json
import os

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
        animal_obj (dict): A dictionary containing animal data (name, diet, locations, type, skin_type).

    Returns:
        str: An HTML string representing the animal as a list item.
    """
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {animal_obj["diet"]}<br/>\n'
    output += f'    <strong>Location:</strong> {", ".join(animal_obj["locations"])}<br/>\n'
    output += f'    <strong>Type:</strong> {animal_obj["type"]}<br/>\n'
    # Check if 'skin_type' key exists before accessing it
    if 'skin_type' in animal_obj and animal_obj['skin_type']:
        output += f'    <strong>Skin Type:</strong> {animal_obj["skin_type"]}<br/>\n'
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
        skin_type = characteristics.get('skin_type') # Get skin_type, might be None

        # Ensure essential data is present
        if all([name, diet, locations, animal_type]) and len(locations) > 0:
            animal_obj = {
                "name": name,
                "diet": diet,
                "locations": locations,
                "type": animal_type,
                # Include skin_type in the object passed to serialize_animal
                # even if it's None, serialize_animal will handle it.
                "skin_type": skin_type
            }
            animals_html += serialize_animal(animal_obj)
        else:
            # Provide more specific feedback if possible
            missing_fields = []
            if not name: missing_fields.append("name")
            if not diet: missing_fields.append("diet")
            if not locations: missing_fields.append("locations")
            if not animal_type: missing_fields.append("type")
            print(f"Skipping animal '{name or 'Unknown'}' due to missing data: {', '.join(missing_fields)}")


    # Replace the placeholder in the template with the generated HTML
    output_html = template.replace('__REPLACE_ANIMALS_INFO__', f'<ul class="cards">\n{animals_html}\n</ul>')

    try:
        with open(output_file, 'w') as f:
            f.write(output_html)
        print(f"Successfully generated '{output_file}'.")
    except Exception as e:
        print(f"Error writing to file '{output_file}': {e}")


def main():
    """
    Main function to orchestrate the loading of data and generation of HTML.
    """
    print("Current working directory:", os.getcwd())

    # Try to list files in the current directory
    try:
        print("Files in current directory:", os.listdir('.'))
    except Exception as e:
        print("Error listing files:", e)

    # Define the expected JSON filename
    json_filename = 'animals_data.json'

    try:
        # Load data from JSON file
        with open(json_filename, 'r') as file:
            animals_data = json.load(file)
            print(f"Successfully loaded {json_filename}")

        # Get and print available skin types (optional analysis)
        skin_types = get_skin_types(animals_data)
        print("Available skin types:", skin_types)

        # Generate the HTML file from the loaded data
        generate_html(animals_data)

    except FileNotFoundError:
        print(f"Error: '{json_filename}' not found in {os.getcwd()}. Make sure the file exists.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_filename}'. Check the file content.")
    except Exception as e:
        # Catch any other unexpected errors during processing
        print(f"An unexpected error occurred: {e}")


# Main execution entry point
if __name__ == "__main__":
    main() # Call the main function