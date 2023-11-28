import numpy as np
import pathlib

TEST_DIR = pathlib.Path("C:\\Users\\ndiur\\sagittal_average\\sagittal_average\\sagittal_brain.py").parent

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

expected = np.zeros(20)
expected[-1] = 1


result = np.loadtxt(TEST_DIR / "brain_average.csv",  delimiter=',')

np.testing.assert_array_equal(result, expected)