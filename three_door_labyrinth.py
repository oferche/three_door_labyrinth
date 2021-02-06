import random

doors = [0, 3, 6]
simulation_results = []
num_of_simulations = 100000

def simulate_escape():
    """Run a single simulation of escape, opening doors until the '0' door is chosen."""
    time_in_labyrinth = 0
    while True:
        current_door = random.choice(doors)
        if current_door == 0:
            time_in_labyrinth += current_door
            simulation_results.append(time_in_labyrinth)
            break
        else:
            time_in_labyrinth += current_door 

# Run the simulation as many times as defined in 'num_of_simulations'.
for i in range (num_of_simulations):
    simulate_escape()

# Calculate and show the average escape time, from all simulations.
avg_escape_time = (sum(simulation_results)/num_of_simulations)
# print(simulation_results)
print()
print(f"Average time to get out of the labyrinth is {round(avg_escape_time, 3)} minutes.")
