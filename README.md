# Monte_Carlo_sim

# Forest Fire Simulation

This repository contains a simulation of forest fire propagation, modeled as a 50x20 grid of trees. The simulation allows customization of wind direction and fire spread probabilities.

## Features
- The fire starts from the northwestern corner of the forest and spreads based on predefined probabilities for neighboring trees.
- Each tree is either **unburned** or **burning**, and the simulation continues until no trees are burning.
- Customizable fire spread probabilities:
  - `p_left`: Probability of catching fire from the left neighbor.
  - `p_right`: Probability of catching fire from the right neighbor.
  - `p_up`: Probability of catching fire from the above neighbor.
  - `p_down`: Probability of catching fire from the below neighbor.

## Requirements
To install the dependencies, run:
