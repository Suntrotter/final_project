import random

# Кількість кидків кубиків
num_rolls = 1000000

# Ініціалізація лічильника для зберігання кількості випадінь кожної суми
sum_count = {i: 0 for i in range(2, 13)}

# Кидання кубиків та підрахунок сум
for _ in range(num_rolls):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total = roll1 + roll2
    sum_count[total] += 1

# Обчислення ймовірностей методом Монте-Карло
probabilities_monte_carlo = {i: count / num_rolls * 100 for i, count in sum_count.items()}

# Виведення результатів
print("Сума\tІмовірність (Монте-Карло)")
for i in range(2, 13):
    print(f"{i}\t{probabilities_monte_carlo[i]:.2f}% ({sum_count[i]}/{num_rolls})")
