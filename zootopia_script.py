import json

# Load data from the 'animals_data.json' file
with open('animals_data.json', 'r') as file:
    animals = json.load(file)

# Create the HTML list of animals in the desired format
html_list = "\n".join(f'''
<li class="cards__item">
  <div class="card__title">{animal.get("name", "Unknown Name")}</div>
  <p class="card__text">
      <strong>Diet:</strong> {animal.get("diet", "Unknown Diet")}<br/>
      <strong>Location:</strong> {animal.get("location", "Unknown Location")}<br/>
      <strong>Type:</strong> {animal.get("type", "Unknown Type")}<br/>
  </p>
</li>
''' for animal in animals)

# Wrap the list in a <ul> element
html_output = f"<ul class='cards'>{html_list}</ul>"

# Write the HTML content to an 'animals.html' file
with open('animals.html', 'w') as file:
    file.write(html_output)

print("HTML file 'animals.html' has been created successfully.")