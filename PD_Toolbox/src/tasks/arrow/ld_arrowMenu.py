# ABore	- 6	Avril 2017
# CRIUGM
# -*- coding: utf-8	-*-

from psychopy import gui  #fetch default gui handler (qt if	available)
from ld_config import arrow_seqA, arrow_seqB, arrow_nbBlocks, arrow_nbKeys,	arrow_durRest, flipMonitor,	fullScreen,	observers, output, subjectPrefix
import os, sys, json, time
import Tkinter

def	getParamMenu(currTask):
	
	if currTask in 'Run2':
		seqFile	= 'arrow_1b_t1t2t3.txt'
	elif currTask in 'Run3':
		seqFile	= 'arrow_2a_t1t3t2.txt'
	elif currTask in 'Run4':
		seqFile	= 'arrow_2b_t1t3t2.txt'
	elif currTask in 'Run5':
		seqFile	= 'arrow_3a_t2t3t1.txt'
	elif currTask in 'Run6':
		seqFile	= 'arrow_3b_t2t3t1.txt'
	elif currTask in 'Run7':
		seqFile	= 'arrow_4a_t2t1t3.txt'
	elif currTask in 'Run8':
		seqFile	= 'arrow_4b_t2t1t3.txt'
	elif currTask in 'Run9':
		seqFile	= 'arrow_5a_t3t1t2.txt'
	elif 'Run10' in currTask:
		seqFile	= 'arrow_5b_t3t1t2.txt'
	elif 'Run11' in currTask:
		seqFile	= 'arrow_6a_t3t2t1.txt'
	elif 'Run12' in currTask:
		seqFile	= 'arrow_6b_t3t2t1.txt'
	elif 'Run1' in currTask:
		seqFile	= 'arrow_1a_t1t2t3.txt'

	# create a	DlgFromDict
	info =	{'Observer':observers,
		'seqFilename':seqFile,
		'durRest':arrow_durRest,
		'language':['French',	'English'],
		'flipMonitor':flipMonitor,
		'fullScreen':fullScreen,
		'subject':subjectPrefix}
	
	infoDlg = gui.DlgFromDict(dictionary=info,	title='Stim	Experiment - v0.1',
		order=['Observer', 'subject', 'seqFilename', 'language', 'flipMonitor', 'fullScreen', 'durRest'],
		tip={'Observer': 'trained	visual observer, initials',	'durRest': 'seconds' , 'flipMonitor':'Doesnt work yet'})

	if	infoDlg.OK:	 # this	will be	True (user hit OK) or False	(cancelled)
		info['language'] = checkLanguage(info['language'])
		json.dump(info, open(os.path.join(output,'arrow',info['subject'] + '_'+currTask+'_'+time.strftime("%Y%m%d-%H%M%S")+'.cfg'),'a+'))
		return info
	else:
		sys.exit("Cancel ARROW")

def	checkLanguage(currLanguage):
	if	currLanguage ==	'French': 
		return 0
	elif currLanguage == 'English':
		return 1
	
# Buttons TASK + COMMANDS RUN
def	createV1(topMenu):
	rest =	Tkinter.Button(topMenu,	text ="Run-v1a_t1t2t3", command=runV1)
	rest.grid(column=0,row=0)

def	runV1():	 
	os.system('python ld_arrowTask.py Run1')
	
def	createV2(topMenu):
	sleepiness	= Tkinter.Button(topMenu, text ="Run-v1b_t1t2t3", command=runV2)
	sleepiness.grid(column=0,row=1)

def	runV2():	   
	os.system('python ld_arrowTask.py Run2')	  
	
def	createV3(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1a_t1t3t2", command=runV3)
	verification.grid(column=0,row=2)
	
def	runV3():	 
	os.system('python ld_arrowTask.py Run3')

def	createV4(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1b_t1t3t2", command=runV4)
	verification.grid(column=0,row=3)
	
def	runV4():	 
	os.system('python ld_arrowTask.py Run4')
	
def	createV5(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1a_t2t3t1", command=runV5)
	verification.grid(column=0,row=4)
	
def	runV5():	 
	os.system('python ld_arrowTask.py Run5')
	
def	createV6(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1b_t2t3t1", command=runV6)
	verification.grid(column=0,row=5)
	
def	runV6():	 
	os.system('python ld_arrowTask.py Run6')	
	
def	createV7(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1a_t2t1t3", command=runV6)
	verification.grid(column=0,row=6)
	
def	runV7():	 
	os.system('python ld_arrowTask.py Run7')	
	
def	createV8(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1b_t2t1t3", command=runV6)
	verification.grid(column=0,row=7)
	
def	runV8():	 
	os.system('python ld_arrowTask.py Run8')	
	
def	createV9(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1a_t3t1t2", command=runV6)
	verification.grid(column=0,row=8)
	
def	runV9():	 
	os.system('python ld_arrowTask.py Run9')	
	
def	createV10(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1b_t3t1t2", command=runV6)
	verification.grid(column=0,row=9)
	
def	runV10():	 
	os.system('python ld_arrowTask.py Run10')	
	
def	createV11(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1a_t3t2t1", command=runV6)
	verification.grid(column=0,row=10)
	
def	runV11():	 
	os.system('python ld_arrowTask.py Run11')	
	
def	createV12(topMenu):
	verification =	Tkinter.Button(topMenu,	text ="Run-v1b_t3t2t1", command=runV6)
	verification.grid(column=0,row=11)
	
def	runV12():	 
	os.system('python ld_arrowTask.py Run12')	
	
def	chooseTask():
	task =	Tkinter.Tk()
	task.title('Arrow Tasks')
	task.grid()
	createV1(task)
	createV2(task)
	createV3(task)
	createV4(task)
	createV5(task)
	createV6(task)
	createV7(task)
	createV8(task)
	createV9(task)
	createV10(task)
	createV11(task)
	createV12(task)
	task.mainloop()
	
if __name__	== "__main__":
	chooseTask()
