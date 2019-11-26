import ants
import os
import numpy as np

root = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/'
all_subjects = ['sub-01', 'sub-02', 'sub-03', 'sub-04', 'sub-05', 'sub-06', 'sub-07', 'sub-08', 'sub-10', 'sub-11', 'sub-12', 'sub-13', 'sub-14', 'sub-15', 'sub-16']
mask = '_CSF_WM_mask_union_bin_shrinked.nii.gz'

for sub in all_subjects:
    sub_dir = root + sub +'/func/'
    mask_dir = root + sub +'/'+ sub +'_ROIs/' +sub + mask
    sub_out_dir = root + sub + '/' + sub + '_ROIs/'

    epi = ants.image_read(os.path.join(sub_dir,sub + '_task-sherlockPart1_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'))
    epi3d = ants.slice_image(epi,axis=3,idx=0)
    noiseROI = ants.image_read(os.path.join(mask_dir))

    reg = ants.registration(fixed=epi3d, moving=noiseROI,type_of_transform='Rigid', reg_iterations = [100,100,20] )
    rAnat = reg['warpedmovout']

    rAnat.to_filename(os.path.join(sub_out_dir, sub + '_CSF_WM_mask_union_shrinked_funcSize.nii.gz'))
