# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:38:11 2019

"""
import pandas as pd 

def read_csv(path):
    
    """
    Read  the dataset of airpolution
    
    """
    df = pd.read_csv(path)
    df= df[['so2','no2']]
    return df


def data_preprocessing(df):
    """
    #Replce  NaN values with 0 
    """
    df[['so2','no2']].replace('NA',0)
    
    """
    #Replce  0 values with mean of column values 
    """
    df[['so2','no2']].replace(0,df.mean())
    
    """
    #fill missing values with mean of column values  
    """
    df.fillna(df.mean(),inplace=True)
    return df 
   
    
def data_manipulation(df,output_path):
    """
    #Changing columns data type to string for manipulation 
    """
    df['no2'] = df['no2'].astype(str)
    df['so2'] = df['so2'].astype(str)
    
    """
    #manipulating Data 
    """
    list_1=[]
    for i in df['no2'].tolist():
        Words=[]
        Words=i.split(".")
        list_1.append(".".join(Words[:2]))
    df['no2']=list_1
    list_1=[]
    for i in df['so2'].tolist():
        Words=[]
        Words=i.split(".")
        list_1.append(".".join(Words[:2]))
    df['so2']=list_1
    
    """
    #Changing columns data type back to float format 
    """
    df['no2'] = df['no2'].astype(float)
    df['so2'] = df['so2'].astype(float)
    
    df = df.sort_values(by=['no2', 'so2'])
    
    """
    #Removing duplicate Values row wise
    """
    df.drop_duplicates(keep ='first', inplace = True)
    
    """
    #Calculating Asthma percentage and including the same to Data set
    """
    asthma=[]
    for row in df.itertuples(index = True, name ='Pandas'):
        number=0
        so2=getattr(row, "so2")
        no2=getattr(row, "no2")
        if so2>no2:
            number=so2/100
        else:
            number=no2/100
        asthma.append(number)
    df['Asthma']=asthma
    
    """
    #Specifying year value in Data set
    """
    Data_count=df.shape[0]
    shape=int(Data_count/20)
    year=[]
    i=1999
    vec=0
    while i <= 2019:
        if Data_count-vec>=shape:
            for x in range(shape):
                year.append(i)
        else:
            for x in range(Data_count-vec):
                year.append(i)
        i += 1
        vec=vec+shape
    df['Year']=year
    
    """
    #Creating final prerocessed csv file
    """
    df.to_csv(output_path,index=False)
    return df

