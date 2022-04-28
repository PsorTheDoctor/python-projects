from sources.Neuron import Neuron


class LinearNetwork:
    def __init__(self, num_of_neurons):
        self.neurons = [0] * num_of_neurons
        for i in range(len(self.neurons)):
            self.neurons[i] = Neuron()

    def initialize_weights(self, initial_weights):
        for i in range(len(self.neurons)):
            self.neurons[i].set_weights(initial_weights[i])

    def response(self, input_signals):
        if input_signals is None:
            print('No data')
        res = [0] * len(self.neurons)
        for i in range(len(self.neurons)):
            res[i] = self.neurons[i].response(input_signals, 'LINEAR')
        return res

    def winner(self, input_signals):
        maximum, res = 0.0, 0.0
        for i in range(len(self.neurons)):
            res = self.neurons[i].response(input_signals, 'LINEAR')
            if abs(res) > maximum:
                maximum = res
        return maximum
