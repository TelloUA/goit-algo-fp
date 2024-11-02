class Item:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

def greedy_algorithm(items: list[Item], capacity: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_calories = 0
    result = []
    for item in items:
        if capacity >= item.cost:
            capacity -= item.cost
            total_calories += item.calories
            result.append(item.name)
    return total_calories, result

def dynamic_programming(budget, items):
    num_items = len(items)
    # формування таблиці по максимальній вартості
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(num_items + 1)]
    # формування таблиці з порядком вибору страв
    item_selection = [[[] for _ in range(budget + 1)] for _ in range(num_items + 1)]

    # Заповнюємо таблицю dp_table знизу вгору
    for i in range(1, num_items + 1):
        for current_budget in range(budget + 1):
            food_cost = items[i - 1].cost
            food_calories = items[i - 1].calories
            
            if food_cost <= current_budget:
                # Варіант, якщо включаємо цей продукт
                include_calories = food_calories + dp_table[i - 1][current_budget - food_cost]
                
                # Варіант, якщо пропускаємо цей продукт
                exclude_calories = dp_table[i - 1][current_budget]
                
                if include_calories > exclude_calories: # вносимо продукт в список
                    dp_table[i][current_budget] = include_calories
                    item_selection[i][current_budget] = item_selection[i - 1][current_budget - food_cost] + [items[i - 1]]
                else: # пропускаємо продукт
                    dp_table[i][current_budget] = exclude_calories
                    item_selection[i][current_budget] = item_selection[i - 1][current_budget]
            else:
                dp_table[i][current_budget] = dp_table[i - 1][current_budget]
                item_selection[i][current_budget] = item_selection[i - 1][current_budget]

    max_calories = dp_table[num_items][budget]
    selected_items = item_selection[num_items][budget]
    selected_items_names = [item.name for item in selected_items]

    return max_calories, selected_items_names

# Дані про їжу
food_items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget_capacity = 90

# підготовка
food_costs = [item["cost"] for item in food_items.values()]
food_calories = [item["calories"] for item in food_items.values()]
num_food_items = len(food_costs)

# підготовка
products = []
for name, info in food_items.items():
    products.append(Item(name, info['cost'], info['calories']))

# результат динамічного програмування
# max_calories = dynamic_programming(budget_capacity, food_costs, food_calories, num_food_items)
max_calories, order = dynamic_programming(budget_capacity, products)
print(f'Результат через функцію динамічного програмування - {max_calories}')
print(f"В наступному порядку вибирались продукти: {", ".join(order)} ")


# результат жадібного алгоритму
total_calories, order = greedy_algorithm(products, budget_capacity)
print(f'Результат через функцію жадібного алгоритму - {total_calories}')
print(f"В наступному порядку вибирались продукти: {", ".join(order)} ")