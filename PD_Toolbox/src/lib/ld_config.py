from __future__ import division
import os

rawFolder = os.getcwd() + os.path.sep

output = os.path.join(rawFolder,'..','..','..','output')
stimuli = os.path.join(rawFolder,'..','..','stimulis')

observers = ['ABoutin', 'EGabitov', 'LGamache','JRatte']
subjectPrefix = 'BioPark_'

#### Pictures
standford_fr = os.path.join(rawFolder,'..','..','stimulis','StanfordSleepinessScale_fr.png')
standford_en = os.path.join(rawFolder,'..','..','stimulis','StanfordSleepinessScale_en.png')
lHandPicture = os.path.join(rawFolder,'..','..','stimulis','lHand.png')
rHandPicture = os.path.join(rawFolder,'..','..','stimulis','rHand.png')

#### WINDOW
fullScreen = True
flipMonitor = False

#### TASKS
### Congruency Parameters
#Visu
congruency_circleLineColor = 'white'
congruency_circleFillColor = 'black'
congruency_circleRadius = 3
congruency_congruentColors = ['gold','blue']

#Experience
congruency_jitter = [0.1, 0.3]
congruency_durRest = 25
###

### MSL Parameters
#Visu

#Experience
msl_nbBlocks = 14
msl_nbKeys = 60
msl_seqA = [1,4,2,3,1]
msl_seqB = [4,1,3,2,4]
msl_nbSeqIntro = 3
msl_durRest = 25
###

### Rhythm Parameters
#Visu

#### EXPYRIMENT

windowSize = (1280, 1024)  # if windowMode is True then use windowSize

goldColor = (255, 215, 0)
textSize = 50
restBGColor = (0, 0, 0)  # expyriment.misc.constants.C_BLACK
restCrossColor = (255, 0, 0)  # expyriment.misc.constants.C_WHITE
regularCrossColor = (0, 255, 0)  # expyriment.misc.constants.C_WHITE
blueCrossColor = (0, 0, 255)  # blue
restCrossSize = (100, 100)
restCrossThickness = 10

activeLineColour = (255, 99, 71)
deactiveLineColour = (211, 211, 211)
lineThickness = 5
startPointLines = [(-25, -75),(-25, -100), (-25, -125)] 
endPointLines = [(25, -75), (25, -100), (25, -125)]



#Experience
rhythm_nbBlocks = 2
rhythm_durRest = 10000
rhythm_bipEach = 2 # s
rhythm_freq = 1/rhythm_bipEach
rhythm_syncDuration=60
rhythm_execLongDuration=60
rhythm_execShortDuration=20
rhythm_imagineDuration=40
###

### Arrow Parameters
#Visu
arrow_circleColor='green'
arrow_circleRadius=1

#Experience
arrow_nbBlocks = 2
arrow_nbKeys = 10
arrow_seqA = [0,2,1,0,3,4,0,1,3,2,4] # Seq between 0 and 4
arrow_seqB = [1,3,2,1,4,0,1,2,4,3,0]
arrow_durRest = 15

arrow_sizePenta = 4.8 #cm
arrow_flipArrow = 0 #72 or 0
###
