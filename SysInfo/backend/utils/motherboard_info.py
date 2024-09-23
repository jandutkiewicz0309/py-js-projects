def find_motherboard_name(data):
    motherboard_name = None

    def traverse_children(children):
        nonlocal motherboard_name
        for child in children:
            if any(brand in child.get('Text', '') for brand in ['ASUS', 'MSI', 'Gigabyte', 'ASRock', 'Intel']):
                motherboard_name = child['Text']
            if 'Children' in child:
                traverse_children(child['Children'])

    traverse_children(data['Children'])

    return motherboard_name
