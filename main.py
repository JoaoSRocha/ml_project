import numpy as np
import pickle
import datetime
import warnings
from classification import *

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # for comb in ['', 'H', 'S', 'C', 'HS', 'HC', 'SC', 'HSC']:
    #     results, table = classic_classifiers(screening=comb)
    #     print(table)
    #results, table = classic_classifiers(screening='')
    #print(table)
    #feature_selection(screening='')

    #select_reduce_classify()
    smoteenn_sffs_reduction_classify_full()

