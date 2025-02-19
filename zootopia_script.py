import json

# Step 1: Load the JSON data
with open('animals_data.json', 'r') as file:
    data = json.load(file)

# Step 2: Generate the animals' data string
output = ''
for animal in data:
    output += f"Name: {animal['name']}\n"
    output += f"Diet: {animal['characteristics'].get('diet', 'N/A')}\n"
    output += f"Location: {', '.join(animal['locations'])}\n"
    output += f"Type: {animal['characteristics'].get('type', 'N/A')}\n\n"

# Step 3: Read the template file
with open('animals_template.html', 'r') as file:
    template_content = file.read()

# Replace the placeholder with the generated animals' data
new_content = template_content.replace('__REPLACE_ANIMALS_INFO__', output)

# Step 4: Write the new content to a new file
with open('animals.html', 'w') as file:
    file.write(new_content)

print("HTML file generated successfully: animals.html")