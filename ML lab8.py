import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def train_network(inputs, targets, learning_rate):
    np.random.seed(1)
    input_hidden_weights = np.random.uniform(-0.5, 0.5, (2, 2))
    hidden_output_weights = np.random.uniform(-0.5, 0.5, (2, 1))
    hidden_bias = np.zeros((1, 2))
    output_bias = np.zeros((1, 1))
    errors = []
    for epoch in range(1000):
        total_error = 0
        for i in range(len(inputs)):
            x = inputs[i].reshape(1, 2)
            target = targets[i].reshape(1, 1)
            hidden_output = sigmoid(
                x @ input_hidden_weights + hidden_bias
            )
            output = sigmoid(
                hidden_output @ hidden_output_weights + output_bias
            )
            error = target - output
            total_error += np.sum(error ** 2)
            output_delta = error * output * (1 - output)
            hidden_delta = (
                hidden_output
                * (1 - hidden_output)
                * (output_delta @ hidden_output_weights.T)
            )
            hidden_output_weights += (
                learning_rate
                * hidden_output.T
                @ output_delta
            )
            output_bias += learning_rate * output_delta
            input_hidden_weights += (
                learning_rate
                * x.T
                @ hidden_delta
            )
            hidden_bias += learning_rate * hidden_delta
        errors.append(total_error)
        if total_error <= 0.002:
            break
    return (
        input_hidden_weights,
        hidden_output_weights,
        hidden_bias,
        output_bias,
        errors
    )
def predict(
    inputs,
    input_hidden_weights,
    hidden_output_weights,
    hidden_bias,
    output_bias
):
    predictions = []
    for x in inputs:
        x = x.reshape(1, 2)
        hidden_output = sigmoid(
            x @ input_hidden_weights + hidden_bias
        )
        output = sigmoid(
            hidden_output @ hidden_output_weights + output_bias
        )
        if output[0][0] >= 0.5:
            predictions.append(1)
        else:
            predictions.append(0)
    return predictions
inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=float)
targets = np.array([
    [0],
    [1],
    [1],
    [0]
], dtype=float)
learning_rate = 0.05
(
    input_hidden_weights,
    hidden_output_weights,
    hidden_bias,
    output_bias,
    errors
) = train_network(
    inputs,
    targets,
    learning_rate
)
predictions = predict(
    inputs,
    input_hidden_weights,
    hidden_output_weights,
    hidden_bias,
    output_bias
)
print("Final error:", errors[-1])
print("Number of iterations:", len(errors))
print("\nXOR Predictions:")
for i in range(len(inputs)):
    print(
        inputs[i].astype(int),
        "Expected:",
        int(targets[i][0]),
        "Predicted:",
        predictions[i]
    )