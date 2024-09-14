# MOnteCArlo -Forest Fire Simulation

This repository contains two implementations of a forest fire simulation. The simulation models the spread of fire across a 50x20 grid of trees with customizable probabilities of fire spreading in different directions.

## Features

### Two-Stage Fire Spread Model:
- **States**: Each tree is either **unburned** (0) or **burning** (1).
- **Fire Spread**: The fire starts from the northwestern corner and spreads to neighboring trees with predefined probabilities.
- The simulation runs until no more trees are burning.
- Statistical data such as the number of burned trees and probability of fire spread is generated.

### Three-Stage Fire Spread Model (With Animation):
- **States**: Each tree can be in one of three states:
  - **Unburned** (0)
  - **Burning** (1)
  - **Burned** (2)
- **Fire Spread**: Similar to the two-stage model, but trees transition through all three states. 
- **Visualization**: The three-stage model includes an animation that visually depicts how the fire spreads across the forest grid over time.
  
## Customizable Parameters
- **Fire Spread Probabilities**:
  - `p_left`: Probability of catching fire from the left neighbor.
  - `p_right`: Probability of catching fire from the right neighbor.
  - `p_up`: Probability of catching fire from the neighbor above.
  - `p_down`: Probability of catching fire from the neighbor below.
  
- **Forest Dimensions**: The simulation is run on a 50x20 grid, but this can be customized in the code.

## Requirements

The simulation code requires the following Python packages:
- `numpy`
- `matplotlib` (for the three-stage model with animation)

You can install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
