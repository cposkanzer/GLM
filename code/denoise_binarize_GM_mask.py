## the noise masks of funcSize are not binarized, this script is to binarize them
import os, json
import nibabel as nib
import numpy as np
from scipy import ndimage

# initalize data
work_dir = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/'
all_subjects = ['sub-01', 'sub-02', 'sub-03', 'sub-04', 'sub-05', 'sub-06', 'sub-07', 'sub-08', 'sub-10', 'sub-11', 'sub-12', 'sub-13', 'sub-14', 'sub-15', 'sub-16']
out_dir = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/'
### work_dir = '/Users/chloe/Documents/output_denoise/'
### all_subjects = ['sub-02']
### out_dir = '/Users/chloe/Documents/'
mask = '_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
mask_thr = 0.5

# iterate through all subjects
for sub in all_subjects:
	for run in range(1,3):
		# generate union mask
		# initialize info
		sub_dir = work_dir + sub + '/' +'func/'
		mask_dir = sub_dir + sub + '_task-sherlockPart' + str(run) + mask
		sub_out_dir = out_dir + sub + '/' + sub + '_ROIs/'

		# load data
		mask_union = nib.load(mask_dir)
		mask_union_affine = mask_union.affine
		mask_union_header = mask_union.header
		mask_union = mask_union.get_data()
		new_mask_union = np.zeros(mask_union.shape)
		
		# make union of the two masks, filter with threshold
		for x in range(0, mask_union.shape[0]):
			for y in range(0, mask_union.shape[1]):
				for z in range(0, mask_union.shape[2]):
					if mask_union[x, y, z] >= mask_thr:
						new_mask_union[x, y, z] = 1
	
		# save the shrinked mask somewhere
		mask_union_img = nib.Nifti1Image(new_mask_union, mask_union_affine, mask_union_header)
		nib.save(mask_union_img, sub_out_dir + sub + '_run' + str(run) +'_GM_mask_bin_funcSize.nii.gz')
