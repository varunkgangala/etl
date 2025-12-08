import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
#Functions 
def extract_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data','raw')
    os.makedirs(data_dir,exist_ok=True)
    df=sns.load_dataset('iris')
    raw_path = os.path.join(data_dir, 'iris.csv')
    df.to_csv(raw_path,index=False)
    return raw_path
if __name__ == '__main__':
    extract_data()




