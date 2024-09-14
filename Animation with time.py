import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Variables
height = 20  # Number of rows (north to south)
width = 50   # Number of columns (west to east)
forest_size = height * width

# Probabilities for fire spreading in different directions
p_left = 0.8   # left neighbor
p_right = 0.3  # right neighbor
p_up = 0.3     # above neighbor
p_down = 0.3   # below neighbor

# House position (northeastern corner)
H = 0  # Row index
W = width - 1  # Column index

# Number of simulations
N_runs = 3800  # Can be changed to 380, 3800, or 38000

# Burn time: how many time slices a tree will burn before it becomes burned
burn_time = 2  # Variable for how long a tree stays in the burning state

# Function to simulate one run with optional history
def simulate_forest(forest_history_on=True):
    forest = np.zeros((height, width), dtype=int)  # 0: unburned, 1: burning, 2: burned
    burn_timer = np.zeros((height, width), dtype=int)  # Timer to track burning duration
    forest[0, 0] = 1  # Fire starts at the northwestern corner
    burn_timer[0, 0] = burn_time

    house_burned = False
    forest_history = [forest.copy()] if forest_history_on else []

    while True:
        burning_trees = (forest == 1)
        if not np.any(burning_trees):
            break  # No more burning trees

        # Create masks for neighboring positions
        left = np.zeros_like(forest, dtype=bool)
        left[:, 1:] = burning_trees[:, :-1]

        right = np.zeros_like(forest, dtype=bool)
        right[:, :-1] = burning_trees[:, 1:]

        up = np.zeros_like(forest, dtype=bool)
        up[1:, :] = burning_trees[:-1, :]

        down = np.zeros_like(forest, dtype=bool)
        down[:-1, :] = burning_trees[1:, :]

        # Unburned trees
        unburned = (forest == 0)

        # Determine which unburned trees catch fire
        catch_fire_left = (left & unburned) & (np.random.rand(height, width) < p_left)
        catch_fire_right = (right & unburned) & (np.random.rand(height, width) < p_right)
        catch_fire_up = (up & unburned) & (np.random.rand(height, width) < p_up)
        catch_fire_down = (down & unburned) & (np.random.rand(height, width) < p_down)

        # Update forest state
        new_burning = catch_fire_left | catch_fire_right | catch_fire_up | catch_fire_down
        forest[new_burning] = 1  # New burning trees
        burn_timer[new_burning] = burn_time  # Set burn time for new burning trees

        # Update burning trees and reduce their burn time
        burn_timer[burning_trees] -= 1
        forest[(burning_trees) & (burn_timer == 0)] = 2  # Trees that have finished burning become burned

        # Check if the house has burned
        if forest[H, W] == 2:
            house_burned = True

        # Add the current forest state to history if recording
        if forest_history_on:
            forest_history.append(forest.copy())

    # Count the number of burned trees
    total_burned = np.sum(forest == 2)

    return total_burned, house_burned, forest_history if forest_history_on else None

# Visualization using matplotlib.animation
def animate_forest_fire(forest_history):
    fig, ax = plt.subplots(figsize=(10, 6))  # Increased figure size
    cmap = plt.get_cmap('YlOrRd', 3)
    cax = ax.matshow(forest_history[0], cmap=cmap, vmin=0, vmax=2)
    fig.colorbar(cax, ticks=[0, 1, 2], label='State (0: Unburned, 1: Burning, 2: Burned)')

    def update(i):
        cax.set_data(forest_history[i])
        ax.set_title(f'Time Step {i}')
        return cax,

    # Create an animation and store it in a variable to avoid garbage collection
    anim = animation.FuncAnimation(fig, update, frames=len(forest_history), interval=500, blit=False, repeat=False)
    plt.show()

# Run the simulation with history
total_burned, house_burned, forest_history = simulate_forest(forest_history_on=True)

# Run the visualization
animate_forest_fire(forest_history)
