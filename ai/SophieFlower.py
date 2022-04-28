# Example 1
# Sophie likes flowers that are fragrant and colorful.
# Fragrance is the first value in both arrays, colorfulness is second.
# Which flowers does Sophie like?

from sources.Neuron import Neuron

feature_weights = [1, 2]
evaluated_object = [3, 2]

examined_neuron = Neuron()
examined_neuron.set_weights(feature_weights)
response = examined_neuron.response(evaluated_object, 'LINEAR')
print(response)

strength = examined_neuron.strength(evaluated_object, 'MANHATTAN')

if abs(response) < 0.2 * strength:
    print("Sophie doesn't know what she wants...")
elif response < 0:
    print("Sophie doesn't like this flower.")
else:
    print("Sophie likes this flower.")
