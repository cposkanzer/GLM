#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:52:51 2019

@author: craigposkanzer
"""
import numpy as np

data_dir = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/'
subjects = (['sub-01','sub-02','sub-03','sub-04','sub-05','sub-06','sub-07',
            'sub-08','sub-10','sub-11','sub-12','sub-13','sub-14','sub-15','sub-16'])
for sub in subjects:
    run1 = np.load(data_dir + sub +'/'+ sub +'_compcorr/'+ sub +'_GM_run_1_compcorr.npy')
    run2 = np.load(data_dir + sub +'/'+ sub +'_compcorr/'+ sub +'_GM_run_2_compcorr.npy')
   
    if sub == 'sub-01':
        run1_edit = np.delete(run1,slice(len(run1)-7,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-11,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-02':
        run1_edit = np.delete(run1,slice(len(run1)-7,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-7,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-03':
        run1_edit = np.delete(run1,slice(len(run1)-6,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-7,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-04':
        run1_edit = np.delete(run1,slice(len(run1)-13,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,6), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-5,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,6), axis = 0)
    if sub == 'sub-05':
        run1_edit = np.delete(run1,slice(len(run1)-8,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-7,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-06':
        run1_edit = np.delete(run1,slice(len(run1)-7,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-7,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-07':
        run1_edit = np.delete(run1,slice(len(run1)-6,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-10,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-08':
        run1_edit = np.delete(run1,slice(len(run1)-5,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-7,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-10':
        run1_edit = np.delete(run1,slice(len(run1)-6,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-8,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-11':
        run1_edit = np.delete(run1,slice(len(run1)-3,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-6,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-12':
        run1_edit = np.delete(run1,slice(len(run1)-5,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-7,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-13':
        run1_edit = np.delete(run1,slice(len(run1)-5,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-6,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-14':
        run1_edit = np.delete(run1,slice(len(run1)-6,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-4,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)
    if sub == 'sub-15':
        run1_edit = np.delete(run1,slice(len(run1)-3,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-4,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)    
    if sub == 'sub-16':
        run1_edit = np.delete(run1,slice(len(run1)-5,len(run1)), axis = 0)
        run1_final = np.delete(run1_edit,slice(0,20), axis = 0)
        run2_edit = np.delete(run2,slice(len(run2)-6,len(run2)), axis = 0)
        run2_final = np.delete(run2_edit,slice(0,20), axis = 0)    
     
        
    np.save(data_dir + sub +'/'+ sub +'_compcorr/' + sub +'_GM_run_1_compcorr_TRedit.npy', run1_final)    
    np.save(data_dir + sub +'/'+ sub +'_compcorr/' + sub +'_GM_run_2_compcorr_TRedit.npy', run2_final)                  
