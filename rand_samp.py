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

def clearEmptyLines(filename):
    command_str = 'sed /^$/d '+ filename #clearing empty lines 
    print command_str
    os.system(command_str)

def samplingDataset(dir,sampsize):
    sample_file_name = 'sample_train_{}.csv'.format(sampsize*182)
    sample_file = open(sample_file_name,'a')  #target file for sample
    is_first = True
    for filename in os.listdir(dir):
        if filename.endswith('.csv'): 
            print filename + '\n'
            unsamped_df = pd.read_csv(os.path.join(dir,filename))       
            samp_df = randomSampleDF(unsamped_df, sampsize)
            print samp_df
#             print >> sample_file, samp_df
            if is_first:
                samp_df.to_csv(sample_file_name,index=False,mode='a',header=True)
                is_first = False
            else:
                samp_df.to_csv(sample_file_name,index=False,mode='a',header=False)
    sample_file.close()
#     clearEmptyLines(sample_file_name)

    

def main():
#     dirname = raw_input('please input dirname:\n')
    samp_size = input('please input sample size:\n')
#     samplingDataset(dirname,samp_size)  #sample 10000 records from each documents
    samplingDataset('/users/luchristopher/documents/ctr_data_cleaned/parsed_train', samp_size)
    
    
if __name__ == '__main__':
    main()
    
