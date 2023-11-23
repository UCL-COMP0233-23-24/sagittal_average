import numpy as np
import sagittal_brain
from sagittal_brain import run_averages

data_input = np.zeros((20, 20))
data_input[-1, :] = 1

np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

# The expeted result is all zeros, except the last one, it should be 1
expected = np.zeros(20)
expected[-1] = 1

run_averages(file_input="brain_sample.csv",
             file_output="brain_average.csv")

TEST_DIR = "/tests"
result = np.loadtxt(TEST_DIR / "brain_average.csv",  delimiter=',')

np.testing.assert_array_equal(result, expected)