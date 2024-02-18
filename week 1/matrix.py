#height weight age
weights = [[0.1, 0.1, -0.3],   # approach
           [0.1, 0.2, 0.0],    # dont care
           [0.0, 1.3, 0.1]]    # run away

def w_sum(a, b):
    assert len(a) == len(b)
    output = 0
    for i in range(len(a)):
        output += a[i] * b[i]
    return output

def vect_mat_mul(vect, matrix):
    assert len(vect) == len(matrix)
    output = [w_sum(vect, matrix[i]) for i in range(len(matrix))]
    return output

def neural_network(input, weights):
    pred = vect_mat_mul(input, weights)
    return pred

height = [8.5, 9.5, 9.9, 9.0]
weight = [0.65, 0.8, 0.8, 0.9]
age = [1.2, 1.3, 0.5, 1.0]
input_data = [height[0], weight[0], age[0]]

pred = neural_network(input_data, weights)
print(pred)
