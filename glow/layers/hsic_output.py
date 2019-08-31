from torch import nn
import glow.activations as activation_module


class HSICoutput(nn.Module):
    """
    Output layer of HSIC architechure for post training purposes.

    """

    def __init__(self, output_dim, loss, activation, learning_rate):
        super().__init__()
        self.args = [output_dim, loss, activation, learning_rate]
        self.output_shape = (output_dim, 1)  # output_dim = number of classes
        self.loss = loss
        self.activation = activation
        self.learning_rate = learning_rate

    def set_input(self, input_shape):
        self.input_shape = input_shape
        self.weights = nn.Linear(self.input_shape[0], self.output_shape[0])

    def forward(self, x):
        return activation_module.get(self.activation)(self.weights(x))
