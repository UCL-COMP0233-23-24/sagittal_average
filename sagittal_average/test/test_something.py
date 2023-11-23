import numpy as np
from ..sagittal_brain import run_averages

def test_analysis():

    np.savetxt('test_input.csv', np.ones((20,20)), fmt='%.1f', delimiter=',')
    np.savetxt('test_output.csv', np.ones((1,20)), fmt='%.1f', delimiter=',')
    run_averages(file_input='test_input.csv', file_output='brain_average.csv' )
    output = np.loadtxt('test_output.csv', dtype=float, delimiter=',') 
    brain_average = np.loadtxt('brain_average.csv', dtype=float, delimiter=',')
    assert np.array_equal(output, brain_average)