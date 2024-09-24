from app.lostark.items import Items
import json


with open('app/lostark/item_sample.json', 'r') as f:
    items = json.loads(f.read())

for item in items:
    it = Items(
        item_name=item.get('item_name'),
        fee=item.get('fee'),
        unit_of_quantity=item.get('unit_of_quantity')
    )
    for material in item.get('materials'):
        it.add_material_list(
            name=material.get('name'),
            quantity=material.get('quantity'),
            price=material.get('price'),
            demand=material.get('demand'),
        )
    it.set_number(1800)
    result = it.get_result()
    print(result)
