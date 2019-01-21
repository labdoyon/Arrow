# -*- coding: utf-8 -*-
# Convert MSL task

import os
import scipy.io as scio
import numpy as np
import json

logFile = '/home/bore/p/PD_Toolbox/output/msl/toto_task_20170515-104025.log'
configFile = '/home/bore/p/PD_Toolbox/output/msl/toto_task_20170515-104025.cfg'

#load json file
cfg = json.loads(open(configFile).read())

#Remove u before field (unicode)
cfg = dict([(str(k),v) for k,v in cfg.items()])

#Conversion of some fields
seq = []
for i in cfg['seq'].split(' - '):
	seq.append(int(i))
cfg['seq'] = seq

obj_arr = np.zeros((int(cfg['nbBlocks'])*int(cfg['nbKeys']) + int(cfg['nbBlocks'])*2 + 1,), dtype=np.object)

index = 0
nBlock = 1

# Load data file
log = open(logFile, 'r')
for line in log: 
	val = line.split()
	val[0] = str(val[0])
	if val[1] in 'StartExp':
		tmpObj = np.zeros((2,), dtype=np.object)
		tmpObj[0] = val[0]
		tmpObj[1] = 'Rest'
		obj_arr[index] = tmpObj
		index += 1
	elif val[1] in 'StartRest':
		tmpObj = np.zeros((2,), dtype=np.object)
		tmpObj[0] = val[0]
		tmpObj[1] = 'Rest'
		obj_arr[index] = tmpObj
		nBlock += 1
		index += 1
	elif val[1] in 'StartPerformance':
		tmpObj = np.zeros((3,), dtype=np.object)
		tmpObj[0] = val[0]
		tmpObj[1] = 'Practice'
		tmpObj[2] = 'Block' + str(nBlock)
		obj_arr[index] = tmpObj
		index += 1
	elif val[1] in 'DATA':
		if not val[3] in '5':
			tmpObj = np.zeros((3,), dtype=np.object)
			tmpObj[0] = val[0]
			tmpObj[1] = 'rep'
			tmpObj[2] = str(val[3])
			obj_arr[index] = tmpObj
			index += 1

# Save
scio.savemat('saved_struct.mat', {'param':cfg, 'logoriginal':obj_arr})