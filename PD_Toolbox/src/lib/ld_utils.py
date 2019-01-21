from psychopy import visual
import tkFileDialog
from ld_config import rawFolder, congruency_circleFillColor, congruency_congruentColors, output
import numpy as np
import os
import time

def createWindow(fullscreen):
    if fullscreen:
		win = visual.Window(screen=1,monitor='testMonitor', color=-1, size=[1024, 768])#size=[1280, 1024])
    else:
		win = visual.Window(screen=0,monitor='testMonitor', color=-1, size=[1024, 768])
    return win

def createOutputFile(mainTask, currTask, currSubject):
	return os.path.join(output, mainTask, currSubject + '_' + currTask + '_' + time.strftime("%Y%m%d-%H%M%S") + '.log')

def getArrowVertices(iVertices):
    oVertices = np.empty([7,2])
    oVertices[0:3] = iVertices[0:3]
    oVertices[2,1] = iVertices[1,1]
    oVertices[3:6] = iVertices[2:5]
    oVertices[5,0] = iVertices[3,0]
    oVertices[6] = iVertices[-1]
    return oVertices

def getCircleColor(key):
    leftColor = congruency_circleFillColor
    rightColor = congruency_circleFillColor
    if key[0]==0:
        leftColor = congruency_congruentColors[int(key[1])]
    else:
        rightColor = congruency_congruentColors[int(key[1])]
    
    return leftColor, rightColor

def readDesign(inputFile):
    design = np.loadtxt(inputFile)
    if design.shape[1]==2:
        print 'Valid design'
        
    return design