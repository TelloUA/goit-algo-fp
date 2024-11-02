import random

def simulate_dice_rolls(num_rolls):
    results_count = {result: 0 for result in range(2, 13)}

    # симуляція
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)  # перший кубик
        die2 = random.randint(1, 6)  # другий кубик
        result_summa = die1 + die2

        results_count[result_summa] += 1

    # зводимо дані в словник з відсотковими значеннями
    probabilities = {result: count / num_rolls for result, count in results_count.items()}
    return probabilities

def theoretical_data():
    # трохи топорно, для порівння
    theory_probs = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36
    }
    return theory_probs

def output_results(simulated_probs, theoretical_probs):    
    for result in range(2, 13):
        sim_prob = simulated_probs.get(result, 0) * 100
        theory_prob = theoretical_probs.get(result, 0) * 100
        diff = sim_prob - theory_prob
        # значення у відсотках
        print(f"{result:^6} | {sim_prob:^12.2f} | {theory_prob:^12.2f} | {diff:^10.2f}")

num_rolls = 100000  # Кількість кидків

simulated_probs = simulate_dice_rolls(num_rolls)
theoretical_probs = theoretical_data()

# Порівняння результатів
output_results(simulated_probs, theoretical_probs)
