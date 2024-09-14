import numpy as np


height = 20  # Number of rows (north to south)
width = 50   # Number of columns (west to east)
forest_size = height * width

# Probabilities for fire spreading in different directions
p_left = 0.8   # left neighbor
p_right = 0.3  # right neighbor
p_up = 0.3     # above neighbor
p_down = 0.3   # below neighbor

# House position (northeastern corner)
H = 0
W = width - 1

# Number of simulations
N_runs = 380

# Function to simulate fire spreading in the forest

def simulate_forest():
    # Initialize forest grid: 0 for unburned, 1 for burning
    forest = np.zeros((height, width), dtype=int)

    forest[0, 0] = 1  # Start fire at northwestern corner

    while True:
        burning_trees = (forest == 1)
        # if not np.any(burning_trees):
        #     break  # Stop if no burning trees left
        # This logic only for 3 state, when there are bured (2) trees

        # Find out the neighbor postions of currently burnng trees
        left = np.zeros_like(forest, dtype=bool)
        left[:, 1:] = burning_trees[:, :-1]

        right = np.zeros_like(forest, dtype=bool)
        right[:, :-1] = burning_trees[:, 1:]

        up = np.zeros_like(forest, dtype=bool)
        up[1:, :] = burning_trees[:-1, :]

        down = np.zeros_like(forest, dtype=bool)
        down[:-1, :] = burning_trees[1:, :]

        # Find unburned trees
        unburned = (forest == 0)

        # Determine which unburned trees catch fire
        catch_fire_left = (left & unburned) & (np.random.rand(height, width) < p_left)
        catch_fire_right = (right & unburned) & (np.random.rand(height, width) < p_right)
        catch_fire_up = (up & unburned) & (np.random.rand(height, width) < p_up)
        catch_fire_down = (down & unburned) & (np.random.rand(height, width) < p_down)

        # Update forest state: new burning trees
        new_burning = catch_fire_left | catch_fire_right | catch_fire_up | catch_fire_down

        # Stop if no new burning trees
        if not np.any(new_burning):
            break

        forest[new_burning] = 1  # Mark new burning trees

    # Count the number of unburned trees
    remaining_unburned = np.sum(forest == 0)
    affected_trees = forest_size - remaining_unburned
    house_burned = forest[H, W] == 1  # Check if the house burned

    return affected_trees, house_burned

# Running the simulation multiple times
def run_simulations(N_runs):
    affected_trees_results = np.zeros(N_runs, dtype=int)
    house_burned_count = 0

    for i in range(N_runs):
        affected_trees, house_burned = simulate_forest()
        affected_trees_results[i] = affected_trees
        if house_burned:
            house_burned_count += 1

    return affected_trees_results, house_burned_count

# Monte Carlo study to analyze the results
def monte_carlo_study():
    # Run simulations and get results
    results, house_burned_count = run_simulations(N_runs)
    #print number of burned tree in all simulation
    #print(results)

    # Minimum and maximum number of burned trees across all simulation
    min_burned_tress = np.min(results)
    print(f"Minimum number of Burned Trees: {min_burned_tress:.4f}")

    max_burned_tress = np.max(results)
    print(f"Maximum number of Burned Trees: {max_burned_tress:.4f}")

    # a) Estimate the the probability that more than 30% of the forest will eventually be burning
    threshold = 0.3 * forest_size
    prob_more_than_30_percent = (np.sum(results > threshold) / N_runs)*100
    print(f"Estimated probability that more than 30% of the forest burns: {prob_more_than_30_percent:.2f} %")

    # b) Predict the total number of affected trees (Avg)
    mean_X = np.mean(results)
    print(f"Estimated total number of affected trees on average: {mean_X:.2f}")

    # c) Estimate std of burning trees
    std_X = np.std(results)
    print(f"Estimated std(X): {std_X:.2f}")

    # Standard error of the mean
    std_error = std_X / np.sqrt(N_runs)
    print(f"Standard error of the estimator: {std_error:.2f}")

    # d) Probability that the actual number of affected trees differs from your estimator by more than 25 trees
    prob_diff_more_than_25 = ( np.sum(np.abs(results - mean_X) > 25) / N_runs )*100
    print(f"Probability that the actual number of affected trees differs from estimator by more than 25 trees: {prob_diff_more_than_25:.2f} %")

    # e) Probability that the house burns
    prob_house_burned = (house_burned_count / N_runs)*100
    print(f"Probability that the house burns: {prob_house_burned:.2f}%")

    # # Advice to the house owner
    # if prob_house_burned > 0.5:
    #     print("Advice: The house is in real danger.")
    # else:
    #     print("Advice: The house is relatively safe.")

# Run the Monte Carlo study
monte_carlo_study()
