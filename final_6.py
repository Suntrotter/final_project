items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Sort items by calories-to-cost ratio in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            total_cost += data['cost']
            total_calories += data['calories']
            selected_items.append(item)
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    # Create a list of items with their cost and calories
    item_list = list(items.items())
    n = len(item_list)
    
    # Create a 2D array to store the maximum calories at each budget
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Fill the dp array
    for i in range(1, n + 1):
        item_name, data = item_list[i - 1]
        item_cost = data['cost']
        item_calories = data['calories']
        for b in range(1, budget + 1):
            if item_cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - item_cost] + item_calories)
            else:
                dp[i][b] = dp[i - 1][b]
    
    # Find the items to include in the optimal solution
    total_cost = 0
    total_calories = dp[n][budget]
    selected_items = []
    b = budget
    
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item_name, data = item_list[i - 1]
            selected_items.append(item_name)
            b -= data['cost']
            total_cost += data['cost']
    
    selected_items.reverse()  # Optional: to get the items in the order they were added
    
    return selected_items, total_cost, total_calories

budget = 100

# Using greedy algorithm
greedy_selected_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", greedy_selected_items)
print("Total cost:", greedy_total_cost)
print("Total calories:", greedy_total_calories)

# Using dynamic programming
dp_selected_items, dp_total_cost, dp_total_calories = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected items:", dp_selected_items)
print("Total cost:", dp_total_cost)
print("Total calories:", dp_total_calories)
