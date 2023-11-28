from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import numpy as np
from sagittal_average.sagittal_brain import run_averages
from art import art 


if __name__ == "__main__":
    parser = ArgumentParser(description="Calculates the average for each sagittal-horizontal plane.",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('file_input', nargs='?', default="brain_sample.csv",
                        help="Input CSV file with the results from scikit-brain binning algorithm.")
    parser.add_argument('--file_output', '-o', default="brain_average.csv",
                        help="Name of the output CSV file.")
    arguments = parser.parse_args()
    message = average(arguments.file_input, arguments.file_output)
    print(art("cute face"), message)

    run_averages(arguments.file_input, arguments.file_output)
