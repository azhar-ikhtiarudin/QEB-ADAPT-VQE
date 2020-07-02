import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
import pandas


if __name__ == "__main__":

    db_e_qe = pandas.read_csv('../../results/adapt_vqe_results/LiH_grad_adapt_pwe_27-Jun-2020_updated.csv')
    db_e_efe = pandas.read_csv('../../results/adapt_vqe_results/LiH_energy_adapt_SDQE_29-Jun-2020.csv')
    # db_g_efe = pandas.read_csv('../../results/adapt_vqe_results/LiH_grad_adapt_EFE_16-Jun-2020.csv')
    # db_g_pwe = pandas.read_csv('../../results/adapt_vqe_results/LiH_grad_adapt_pwe_27-Jun-2020.csv')

    plt.plot(db_e_qe['cnot_count'], db_e_qe['error'], label='energy_based_qe')
    plt.plot(db_e_efe['cnot_count'], db_e_efe['error'], label='energy_based_efe')
    # plt.plot(db_g_efe['cnot_count'], db_g_efe['error'], label='grad_based_efe')
    # plt.plot(db_g_pwe['cnot_count'], db_g_pwe['error'], label='grad_based_pwe')

    plt.legend()
    plt.yscale('log')

    plt.show()

    print('macaroni')
