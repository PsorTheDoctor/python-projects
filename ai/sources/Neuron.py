from math import sqrt, exp, tanh


class Neuron:
    def __init__(self):
        self.weights = []
        self.prev_weights = []

    def set_weights(self, weights):
        self.weights = weights

    @staticmethod
    def activation_function(arg, func):
        if func == 'LINEAR':
            return arg
        elif func == 'BIPOLAR':
            if arg > 0:
                return 1
            else:
                return -1
        elif func == 'SIGMOIDAL':
            beta = 1.0
            return 1.0 / 1.0 + exp(-beta * arg)
        elif func == 'TANH':
            return tanh(arg)

    def response(self, input_signals, func):
        if input_signals is None or len(input_signals) != len(self.weights):
            print('The signal array must have the same length as the weight array.')

        result = 0.0
        for i in range(len(self.weights)):
            result += self.weights[i] * input_signals[i]
        return self.activation_function(result, func)

    @staticmethod
    def strength(signals, norm):
        strength = 0.0
        if norm == 'MANHATTAN':
            for s in signals:
                strength += abs(s)
            return strength
        elif norm == 'EUCLIDEAN':
            for s in signals:
                strength += s * s
            return sqrt(strength)
        else:
            return 0.0
