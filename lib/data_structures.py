spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    # Use list comprehension to extract the 'name' field from each dictionary
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    # Filter the foods where the 'heat_level' is greater than 5
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    # Loop through each food and use print to display name, cuisine, and heat level
    for food in spicy_foods:
        heat_level = (
            "🌶" * food["heat_level"]
        )  # Repeat the 🌶 emoji according to heat level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Loop through and find the first food that matches the cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    # Use the get_spiciest_foods function and print the result using print_spicy_foods
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    # Calculate the total heat levels and divide by the number of foods
    total_heat = sum([food["heat_level"] for food in spicy_foods])
    return total_heat // len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    # Append the new spicy food to the list and return the updated list
    spicy_foods.append(spicy_food)
    return spicy_foods
