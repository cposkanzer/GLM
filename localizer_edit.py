#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:01:28 2019

@author: craigposkanzer
"""
#this script takes the TR edited data and cuts out the first  
#5 minutes (approx.) for localizing 


import numpy as np
import nibabel as nib
from nilearn.input_data import NiftiMasker

data_dir = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/'
subjects = (['sub-01','sub-02','sub-03','sub-04','sub-05','sub-06','sub-07',
            'sub-08','sub-10','sub-11','sub-12','sub-13','sub-14','sub-15','sub-16'])
#raw_img = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/sub-01/func/sub-01_task-sherlockPart1_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'
mask = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/gm_bin_mask.nii.gz'


#raw = nib.load(raw_img)
#raw_hdr = raw.header
mfn = nib.load(mask)
#masker = NiftiMasker()
#masker.fit(mfn)

for sub in subjects:
    masker = NiftiMasker()
    masker.fit(mfn)
    run1 = np.load(data_dir + sub +'/'+ sub +'_compcorr/'+ sub +'_GM_run_1_compcorr_TRedit.npy')
    raw_img = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/' + sub + '/func/' + sub + '_task-sherlockPart1_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz' 
    raw = nib.load(raw_img)
    #raw_hdr = raw.header
   
    localizer_data = run1[0:204,:]
    nifti = masker.inverse_transform(localizer_data)
    nifti_data  = nifti.get_data()
    nifti_array = np.array(nifti_data)
    final_img = nib.Nifti1Image(nifti_array, mfn.affine, raw.header)   
    #print(nifti.header.get_zooms())
    #nib.Nifti1Header.from_header(header = hdr, check = True)
    #final_img = nib.Nifti1Image(nifti,affine)
    nib.save(final_img, data_dir + sub +'/'+ sub +'_compcorr/' + sub +'_GM_run_1_compcorr_localizer.nii.gz') 
