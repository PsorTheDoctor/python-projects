# Example program to predict if an animal is mammal, bird or fish.
#
# The input array contains:
# 1. How many legs does an animal have?
# 2. Is it live in water?
# 3. Can it fly?
# 4. Is it covered with feathers?
# 5. Is it oviparous (born from eggs)?

from sources.LinearNetwork import LinearNetwork

mammal = [4.0, 0.01, 0.01, -1.0, -1.5]
bird = [2.0, -1.0, 2.0, 2.5, 2.0]
fish = [-1.0, 3.5, 0.01, -2.0, 1.5]
weights = [mammal, bird, fish]

examined_network = LinearNetwork(3)
examined_network.initialize_weights(weights)

fox = [4.0, -1.0, -1.0, -0.9, -1.0]
res = examined_network.response(fox)
print(res)

winner = examined_network.winner(fox)
print(winner)
