# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:49:47 2019

@author: GR5048890
"""
import modelling
import config
import preprocessing
import unit_testcase
import visualization
if __name__ == '__main__':

    df = preprocessing.read_csv(config.input_path)
    df = preprocessing.data_preprocessing(df)
    df = preprocessing.data_manipulation(df,config.output_path)
    visualization.visualization_raw_data(df,config.image_url)
    X_test,y_pred_asthama,clf = modelling.spliting_data_and_training_model(config.output_path,df)
    modelling.visualization(X_test,y_pred_asthama)
    so2=input("please enter So2 value= ")
    no2=input("please enter No2 value= ")
    unit_testcase.unit_test_case(clf,so2,no2)