def cookbook(*info):
    final_information = {}
    for el in info:
        recipe_name, cuisine, ingredients = el
        if cuisine not in final_information:
            final_information[cuisine] = {}
        if recipe_name not in final_information[cuisine]:
            final_information[cuisine][recipe_name] = []
        final_information[cuisine][recipe_name] = ingredients
    result = ''
    for cuisine_name, recipe_info in sorted(final_information.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f'{cuisine_name} cuisine contains {len(recipe_info)} recipes:\n'

        for recipe, ingredients in sorted(recipe_info.items(), key=lambda x: x[0]):
            result += f'  * {recipe} -> Ingredients: {", ".join(el for el in ingredients)}\n'

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
