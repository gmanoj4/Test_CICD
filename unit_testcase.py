# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:52:50 2019

@author: GR5048890
"""
import numpy as np
def unit_test_case(clf,so2,no2):
    data=[]
    data.append(int(so2))
    data.append(int(no2))
    x_t = np.array(data).reshape(1,2)
    testing= clf.predict(x_t)
    print("Asthma Predection = ",testing[0][0],"%")