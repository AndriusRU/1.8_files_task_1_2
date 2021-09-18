from pprint import pprint


def create_dict_from_file(file_name: str) -> dict:
    result = {}
    with open(file_name, 'r', encoding='utf-8') as file_recipes:
        for line in file_recipes:
            dish = line.strip()
            count_ingredients = int(file_recipes.readline())
            list_ingredients = []
            for item in range(count_ingredients):
                ingredient_name, quantity, measure = file_recipes.readline().split('|')
                list_ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            result[dish] = list_ingredients
            file_recipes.readline()
    return result

# pprint(create_dict_from_file('recipes.txt'))


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    result = {}

    for dish, list_ingr in create_dict_from_file('recipes.txt').items():
        if dish in dishes:
            for ingr in list_ingr:
                ingredient = ingr.get('ingredient_name')
                if result.get(ingredient) is not None:
                    current_quantity = int(result[ingredient]['quantity']) + int(ingr.get('quantity')) * person_count
                else:
                    current_quantity = int(ingr.get('quantity')) * person_count
                result[ingr.get('ingredient_name')] = {'measure': ingr.get('measure'), 'quantity': current_quantity}
    return result


pprint(get_shop_list_by_dishes(['Омлет', 'Яичница'], 3))
