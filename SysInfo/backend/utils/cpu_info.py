def get_cpu_name(data):
    """
    Funkcja do pobrania nazwy procesora z danych JSON.
    """
    cpu_name = None

    def traverse_children(children):
        nonlocal cpu_name
        for child in children:
            if ("AMD" in child.get('Text', '') and "Ryzen" in child.get('Text', '')) or "Intel" in child.get('Text', ''):
                cpu_name = child['Text']
            if 'Children' in child:
                traverse_children(child['Children'])

    traverse_children(data['Children'])

    return cpu_name


def get_cpu_temperature(data):
    """
    Funkcja do pobrania temperatury procesora z danych JSON.
    """
    temperatures = []

    def traverse_children(children):
        nonlocal temperatures
        for child in children:
            if "Temperatures" in child.get('Text', ''):
                for sensor in child['Children']:
                    if "CPU" in sensor.get('Text', ''):
                        temperatures.append({
                            "sensor": sensor['Text'],
                            "temperature_celsius": sensor['Value']
                        })
            if 'Children' in child:
                traverse_children(child['Children'])

    traverse_children(data['Children'])

    return temperatures
