#------------------------------------------------------------------------------
# SETUP FOR ARTICLE ...
# @ Leonardo Lavagna 2024
#------------------------------------------------------------------------------


from qiskit import Aer


# code_path (str): local path of the quantum optimization routines
code_path = ""

# results_path (str): local path where the results are sotred
results_path = ""

# figures_path (str): local path where the figures are sotred
figures_path = ""

# data_path (str): local path where the dataset is sotred
data_path = ""

#seed (int): A seed for the pseudorandom generators (needed for reproducibility)
seed = 123

#shots (int): Number of measurements of each quantum circuit executed.
shots = 1024

#verbose (bool): A boolean variable that allows to work in debugging mode if True.
verbose = False

#backend (Qiskit backend): A Qiskit backend to simulate a quantum device.
backend = Aer.get_backend("aer_simulator")

#mixer (str): Type of qaoa mixer operator. Currently are available 'x', 'y', 'xx', 'xy' and 'yy' mixers.
mixer = "x" 

#method (str): Type of optimization method to be used with `scipy.optimize.minimize`. Available 'BFGS', 'L-BFGS-B', 'COBYLA' and 'SLSQP'.
method = 'COBYLA' 