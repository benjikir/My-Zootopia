import json

def load_data(file_path):
    """ Lädt eine JSON-Datei """
    with open(file_path, "r") as handle:
        return json.load(handle)

# Daten aus der JSON-Datei laden
animals_data = load_data('animals_data.json')

# Jedes Tier in der gewünschten Formatierung ausgeben
for animal in animals_data:
    name = animal.get('name', 'Unknown')
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet', 'Unknown')
    locations = animal.get('locations', ['Unknown'])
    animal_type = characteristics.get('type', 'Unknown')

    # Formatierte Ausgabe
    print(f"Name: {name}")
    print(f"Diet: {diet}")
    print(f"Location: {', '.join(locations)}")
    print(f"Type: {animal_type}")
    print()  # Leerzeile zwischen den Tieren