'''
    Process to emulate the send of tweets in real time enviroment
'''
import time

import pandas as pd


def get_data_from_file(filename):
    '''
        Get a data in data frame format from file.
        
        Args
        filename (string): location of file
        
        return a data frame
    '''
    return pd.read_csv(filename, encoding="latin9")



print(get_data_from_file("./sample_data/database.csv"))