#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:52:27 2019

@author: craigposkanzer
"""
#this script corregisters and averages the GM probabilites across subjects

import numpy as np
import nibabel as nib
import ants
import os


root = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/'
sublist=(['sub-02','sub-03','sub-04','sub-05','sub-06','sub-07',
            'sub-08','sub-10','sub-11','sub-12','sub-13','sub-14','sub-15','sub-16'])
num_subs = 15
mask_thresh = .1


gm_mask = ants.image_read(os.path.join(root,'sub-01/anat/sub-01_space-MNI152NLin2009cAsym_label-GM_probseg.nii.gz'))
funcROI = ants.image_read(os.path.join(root, 'sub-01/func/sub-01_task-sherlockPart1_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'))
epi3d = ants.slice_image(funcROI,axis=3,idx=0)
reg = ants.registration(fixed=epi3d, moving=gm_mask,type_of_transform='Rigid', reg_iterations = [100,100,20] )
gm_mask_size = reg['warpedmovout']


for sub in sublist:
    sub_dir = root + sub +'/func/'
    data_dir = root + sub + '/anat/'
    sub_mask = ants.image_read(os.path.join(data_dir,sub + '_space-MNI152NLin2009cAsym_label-GM_probseg.nii.gz'))
    funcROI = ants.image_read(os.path.join(sub_dir, sub + '_task-sherlockPart1_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'))
    epi3d = ants.slice_image(funcROI,axis=3,idx=0)
    reg = ants.registration(fixed=epi3d, moving=sub_mask,type_of_transform='Rigid', reg_iterations = [100,100,20] )
    sub_mask_size = reg['warpedmovout']
    gm_mask_size = gm_mask_size + sub_mask_size
   
    
gm_mask_size = gm_mask_size/num_subs

#mask_affine = gm_mask.affine
#mask_header = gm_mask.header
#mask_data = gm_mask.get_data()
#bin_mask= np.zeros(gm_mask.shape)
#print(bin_mask.shape)

# make union of the two masks, filter with threshold
#for x in range(0, gm_mask.shape[0]):
#    for y in range(0, gm_mask.shape[1]):
#        for z in range(0, gm_mask.shape[2]):
#            if gm_mask[x, y, z] >= mask_thresh:
#                bin_mask[x, y, z] = 1
           
gm_mask_size.to_filename(os.path.join(root, 'gm_mask_avg.nii.gz'))

