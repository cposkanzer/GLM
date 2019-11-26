# filter out data from GM masks
import os, json, time
import nibabel as nib
import numpy as np

# initalize data
work_dir = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/'
all_subjects = ['sub-01', 'sub-02', 'sub-03', 'sub-04', 'sub-05', 'sub-06', 'sub-07', 'sub-08', 'sub-10', 'sub-11', 'sub-12', 'sub-13', 'sub-14', 'sub-15', 'sub-16']
### work_dir = '/Users/chloe/Documents/'
#all_subjects = ['sub-01', 'sub-02', 'sub-03']
mask_dir = '/gsfs0/data/poskanzc/Sherlock/preproc/fmriprep/gm_bin_mask.nii.gz'
total_run = 2

#load mask
mask = nib.load(mask_dir).get_data()

# iterate through all subjects
for sub in all_subjects:

	# initialize data
	sub_dir = work_dir + sub + '/'
	sub_out_dir = sub_dir + sub + '_pre/'
	#mask_dir = sub_dir + sub + '_ROIs/' + sub + '_GM_mask_bin_funcSize.nii.gz'
	if not os.path.exists(sub_out_dir):
		os.makedirs(sub_out_dir)
	
	# load mask
	#mask = nib.load(mask_dir).get_data()

	# load the data from all runs
	for run in range(1, total_run + 1):
		#mask_dir = sub_dir + sub + '_ROIs/' + sub + '_run'+ str(run)+ '_GM_mask_bin_funcSize.nii.gz'
		#mask = nib.load(mask_dir).get_data()
		# print('run number: ' + str(run))
		
		# initialize data
		run_dir = sub_dir + 'func/' + sub + '_task-sherlockPart' + str(run) + '_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'
		run_data = nib.load(run_dir).get_data()
		noise_data = np.zeros((run_data.shape[3], int(mask.sum())))

		t1 = time.time()

		'''
		# filter noise data
		mask = np.expand_dims(mask, 3).repeat(run_data.shape[3], axis=3)
		run_data_temp = run_data.reshape([-1])
		# print(run_data_temp.shape)
		mask_temp = mask.reshape([-1])
		# print(mask.sum())
		# print(mask_temp[1:4, 3:8])
		print(mask_temp.shape)
		# print(run_data_temp.shape)
		pair = zip(run_data_temp.tolist(), mask_temp.tolist())
		noise_data = np.array([x for (x, y) in pair if y == 1]).reshape([-1, run_data.shape[3]]).T
		''' 

		# iterate through current data matrix
		for t in range(0, run_data.shape[3]):
			col_index = 0
			for x in range(0, run_data.shape[0]):
				for y in range(0, run_data.shape[1]):
					for z in range(0, run_data.shape[2]):
						if mask[x, y, z] == 1:
							noise_data[t, col_index] = run_data[x, y, z, t]
							col_index += 1

		t2 = time.time()
		# print(t2 - t1)

		# save to file
		# print('saved noise_data shape')
		# print(noise_data.shape)
		# print(x + 1)
		np.save(sub_out_dir + sub + '_GM_' + 'run_' + str(run) + '.npy', noise_data)
