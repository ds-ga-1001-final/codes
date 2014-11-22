'''
Created on Nov 20, 2014

@author: luchristopher
'''
import sys
import numpy as np
import pandas as pd
import random
import os

'''Sampling the dataframe'''
def randomSampleDF(df,sampsize):
    indices = random.sample(df.index,sampsize)
    return df.ix[indices]

def samplingDataset(dir,sampsize):
    sample_file = open('sample_train.csv','a')  #target file for sample
    for filename in os.listdir(dir):
        if filename.endswith('.csv'): 
            unsamped_df = pd.read_csv(filename)       
            samp_df = randomSampleDF(unsamped_df, sampsize)
            print >> sample_file, samp_df
    sample_file.close()
    

def main():
    dirname = raw_input('please input dirname:\n')
    samp_size = input('please input sample size:\n')
    samplingDataset(dirname,samp_size)  #sample 10000 records from each documents
    
    
if __name__ == '__main__':
    main()
    
