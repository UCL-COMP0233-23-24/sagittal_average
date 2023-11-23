import numpy as np
from sagittal_brain import run_averages


# input should be the calculated average
import numpy as np

data_input = np.zeros((20, 20))
data_input[-1, :] = 1

np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

run_averages('brain_sample.csv', 'brain_average.csv')

# output is actual average 
expected = [0.0] * 19 + [1.0]

brain_average = np.loadtxt('brain_average.csv', dtype=float, delimiter=',')

print(np.loadtxt('brain_average.csv', dtype=int, delimiter=','))
print(expected)

np.testing.assert_array_equal(brain_average, expected)




