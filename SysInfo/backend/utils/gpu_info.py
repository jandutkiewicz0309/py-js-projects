def get_gpu_info(data):
    """
    Funkcja do pobierania obciążenia i temperatury karty graficznej.
    """
    gpu_usage = None
    gpu_temperature = None

    def traverse_children(children):
        nonlocal gpu_usage, gpu_temperature
        for child in children:
            if "Load" in child.get('Text', ''):
                for sensor in child['Children']:
                    if "GPU Core" in sensor.get('Text', ''):
                        gpu_usage = sensor['Value']
            if "Temperatures" in child.get('Text', ''):
                for sensor in child['Children']:
                    if "GPU" in sensor.get('Text', ''):
                        gpu_temperature = sensor['Value']
            if 'Children' in child:
                traverse_children(child['Children'])

    traverse_children(data['Children'])

    return gpu_usage, gpu_temperature
