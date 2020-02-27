import pandas as pd


def and_perceptron(v1, v2):
    weight1 = 1
    weight2 = 4
    bias = -5
    return 1 if weight1 * v1 + weight2 * v2 + bias >= 0 else 0
    pass


def or_perceptron(v1, v2):
    weight1 = 3
    weight2 = 1
    bias = -1
    return 1 if weight1 * v1 + weight2 * v2 + bias >= 0 else 0


def not_perceptron(v):
    weight = -1.0
    bias = 0.0
    return 1 if weight * v + bias >= 0 else 0


def xor_perceptron(v1, v2):
    and_out = and_perceptron(v1,v2)
    not_and_out = not_perceptron(and_out)
    or_out = or_perceptron(v1,v2)
    return and_perceptron(not_and_out, or_out)


if __name__ == "__main__":

    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    correct_outputs = [False, True, True, False]
    outputs = []

    for test_input, correct_output in zip(test_inputs, correct_outputs):
        output = xor_perceptron(test_input[0], test_input[1])
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1],
                        output, is_correct_string])
    num_wrong = len([output[3] for output in outputs if output[3] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=[
                                'Input 1', '  Input 2', '  Activation Output', '  Is Correct'])
    if not num_wrong:
        print('Nice!  You got it all correct.\n')
    else:
        print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))
