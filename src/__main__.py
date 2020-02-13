from src.vqe_runner import VQERunner
from src.molecules import H2, LiH, HF
from src.ansatz_elements import UCCGSD, UCCSD, HardwareEfficientAnsatz1, HardwareEfficientAnsatz2
from src.backends import QiskitSimulation
from src.utils import LogUtils

import logging
import time
import numpy
import pandas
import datetime
import qiskit


if __name__ == "__main__":

    molecule = H2
    r = 0.735
    max_n_iterations = 2000

    # logging
    LogUtils.log_cofig()

    # ansatz_elements = UCCSD(molecule.n_orbitals, molecule.n_electrons).get_ansatz_elements()
    ansatz_element = HardwareEfficientAnsatz2(molecule.n_orbitals, molecule.n_electrons).get_ansatz_element()
    ansatz_elements = [ansatz_element, ansatz_element, ansatz_element]

    vqe_runner = VQERunner(molecule, backend=QiskitSimulation, ansatz_elements=ansatz_elements,
                           molecule_geometry_params={'distance': r}, optimizer='Nelder-Mead')

    t0 = time.time()
    result = vqe_runner.vqe_run(max_n_iterations=max_n_iterations)
    t = time.time()

    logging.critical(result)
    print(result)
    print('TIme for running: ', t - t0)

    print('Pizza')
