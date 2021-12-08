import numpy as np
inputs = open('input', 'r')

crabs = [int(x.strip()) for x in inputs.read().split(',')]

crabs = np.array(crabs)
fuel_costs = np.zeros((max(crabs)))

min = np.inf
cost_matrix = np.zeros((max(crabs)+1))
for i,v in enumerate(cost_matrix):
    cost_matrix[i] = np.sum(np.arange(i+1))

for idx in range(max(crabs)):
    current = np.sum(cost_matrix[np.abs(idx-crabs)])
    if current < min:
        min = current
print(min)