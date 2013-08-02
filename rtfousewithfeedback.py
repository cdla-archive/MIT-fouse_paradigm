#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.76.00), Thu Jul 18 10:06:46 2013
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from scripts.query_murfi import Murfi
from math import floor, fabs
from glob import glob
import math

murfi_IP = '192.168.2.5'
murfi_PORT = 15001
murfi_TR = 127


num_triggers=5



# Store info about the experiment session
expName = 'rtfousewithfeedback'  # from the Builder filename that created this script
expInfo_init= { u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo_init, title=expName, order=['participant','session'])#,'V1:faces','V2:scenes','V3:50/50faces','V4:50/50scenes'])
if dlg.OK == False: 
    core.quit()  # user pressed cancel

if int(expInfo_init['session'])==1:
    expInfo={u'participant':u'%s'%expInfo_init['participant'],u'session':u'%s'%expInfo_init['session'],u'V1:faces':u'',u'V2:scenes':u'',u'V3:50/50faces':u'',u'V4:50/50scenes':u''}
    dlg2=gui.DlgFromDict(dictionary=expInfo, title=expName, order=['participant','session','V1:faces','V2:scenes','V3:50/50faces','V4:50/50scenes'],fixed=['participant','session'])
else:
    if os.path.isfile(glob('data'+ os.path.sep + 'baseline_values' + os.path.sep + 'subject%s*'%(expInfo_init['participant']))[-1]):
        print 'using previous baseline values'
        previous_baselines = np.genfromtxt(glob('data'+ os.path.sep + 'baseline_values' + os.path.sep + 'subject%s*'%(expInfo_init['participant']))[-1])
        expInfo={u'participant':u'%s'%expInfo_init['participant'],u'session':u'%s'%expInfo_init['session'],u'V1:faces':u'%s'%previous_baselines[0],u'V2:scenes':u'%s'%previous_baselines[1],u'V3:50/50faces':u'%s'%previous_baselines[2],u'V4:50/50scenes':u'%s'%previous_baselines[3]}
        dlg2=gui.DlgFromDict(dictionary=expInfo, title=expName, order=['participant','session','V1:faces','V2:scenes','V3:50/50faces','V4:50/50scenes'],fixed=['participant','session'])
        #expInfo['V1:faces']=previous_baselines[0]
        #expInfo['V2:scenes']=previous_baselines[1]
        #expInfo['V3:50/50faces']=previous_baselines[2]
        #expInfo['V4:50/50scenes']=previous_baselines[3]
if dlg2.OK == False: 
    core.quit()  # user pressed cancel

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

vector_indices=[[16,33],[45,62],[73,90],[101,118]]
goodfeedback=0
badfeedback=0
face_scene_conditions=[]
fbs=[]
# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
if expInfo['participant']=='debug' or expInfo['participant']=='debugtiming':
    filename = 'data' + os.path.sep +'debug' + os.path.sep + '%s_%s_%s_%s' %(expInfo['participant'], expInfo['date'],expName,expInfo['session'])
else:
    filename = 'data' + os.path.sep + '%s_%s_%s_%s' %(expInfo['participant'], expInfo['date'],expName,expInfo['session'])
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)


# Setup the Window
timings={}
if expInfo['participant']=='debug':
    win=win = visual.Window(size=(800,600), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
    timings['baseline']= 1
    timings['stimulus']=1
    timings['fixation']=1
    timings['fixation_2']=1
    murfi_FAKE = True
    print "**********DEBUG MODE************"
    if int(expInfo['session'])==1:
        expInfo['V2:scenes']='-1'
        expInfo['V1:faces']='.3'
        expInfo['V4:50/50scenes']='0'
        expInfo['V3:50/50faces']='0'
elif expInfo['participant']=='debugtiming':
    win = visual.Window(size=(1024,768), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
    timings['baseline']=30
    timings['stimulus']=11.5
    timings['fixation']=4
    timings['fixation_2']=10
    murfi_FAKE = True
    print "*************DEBUG TIMING MODE***************"
    expInfo['V2:scenes']='-1'
    expInfo['V1:faces']='1'
    expInfo['V4:50/50scenes']='0'
    expInfo['V3:50/50faces']='0'
else:
    win = visual.Window(size=(1024,768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
    timings['baseline']=30
    timings['stimulus']=11.5
    timings['fixation']=4
    timings['fixation_2']=10

#if int(expInfo['session']) != 1:
#    if os.path.isfile(glob('data'+ os.path.sep + 'baseline_values' + os.path.sep + 'subject%s*'%(expInfo['participant']))[-1]):
#        print 'hurray'
#        previous_baselines = np.genfromtxt(glob('data'+ os.path.sep + 'baseline_values' + os.path.sep + 'subject%s*'%(expInfo['participant']))[-1])
#        expInfo['V1:faces']=previous_baselines[0]
#        expInfo['V2:scenes']=previous_baselines[1]
#        expInfo['V3:50/50faces']=previous_baselines[2]
#        expInfo['V4:50/50scenes']=previous_baselines[3]

murfi = Murfi(murfi_IP, murfi_PORT, murfi_TR, murfi_FAKE)
recs=[]
def makeFBrecs(zero_val,fb,fillColor=None,xoffset=0):
    if thisTrial.instruction_text=='Attend to Scenes':
        if fb >=zero_val:
            rec_height=1*(fb-zero_val)/(30*(max-zero_val))*.5
            for idx in range(30):
                rec=visual.ShapeStim(win, closeShape=True, vertices=((xoffset-.125,idx*rec_height),(xoffset+.125,idx*rec_height),(xoffset+.125,(idx+1)*rec_height),(xoffset-.125,(idx+1)*rec_height)),depth=-3,opacity=1,fillColor='Red',lineColor='Red')
                recs.append(rec)
        elif fb<zero_val:
            rec_height=(fb-zero_val)/(30*(min-zero_val))*.5
            for idx in range(30):
            #rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*rec_height),(.125,idx*rec_height),(.125,(idx+1)*rec_height),(-.125,(idx+1)*rec_height),depth=1,opacity=1,fillColor='Green')
                rec=visual.ShapeStim(win, closeShape=True, vertices=((xoffset-.125,idx*-1*rec_height),(xoffset+.125,idx*-1*rec_height),(xoffset+.125,(idx+1)*-1*rec_height),(xoffset-.125,(idx+1)*-1*rec_height)),depth=-3,opacity=1,fillColor='Green',lineColor='Green')
                recs.append(rec)
     #   if fb <=zero_val:
      #      rec_height=-1*(fb-zero_val)/(30*(max-zero_val))*.5
      #      for idx in range(30):
      #          rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*rec_height),(.125,idx*rec_height),(.125,(idx+1)*rec_height),(-.125,(idx+1)*rec_height)),depth=-3,opacity=1,fillColor='Green',lineColor='Green')
      #          recs.append(rec)
      #  elif fb>zero_val:
      #      rec_height=-1*(fb-zero_val)/(30*(min-zero_val))*.5
      #      for idx in range(30):
      #      #rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*rec_height),(.125,idx*rec_height),(.125,(idx+1)*rec_height),(-.125,(idx+1)*rec_height),depth=1,opacity=1,fillColor='Green')
      #          rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*-1*rec_height),(.125,idx*-1*rec_height),(.125,(idx+1)*-1*rec_height),(-.125,(idx+1)*-1*rec_height)),depth=-3,opacity=1,fillColor='Red',lineColor='Red')
      #          recs.append(rec)
    if thisTrial.instruction_text=='Attend to Faces':
        if fb >=zero_val:
            rec_height=1*(fb-zero_val)/(30*(max-zero_val))*.5
            for idx in range(30):
                rec=visual.ShapeStim(win, closeShape=True, vertices=((xoffset-.125,idx*rec_height),(xoffset+.125,idx*rec_height),(xoffset+.125,(idx+1)*rec_height),(xoffset-.125,(idx+1)*rec_height)),depth=-3,opacity=1,fillColor='Green',lineColor='Green')
                recs.append(rec)
        elif fb<zero_val:
            rec_height=(fb-zero_val)/(30*(min-zero_val))*.5
            for idx in range(30):
            #rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*rec_height),(.125,idx*rec_height),(.125,(idx+1)*rec_height),(-.125,(idx+1)*rec_height),depth=1,opacity=1,fillColor='Green')
                rec=visual.ShapeStim(win, closeShape=True, vertices=((xoffset-.125,idx*-1*rec_height),(xoffset+.125,idx*-1*rec_height),(xoffset+.125,(idx+1)*-1*rec_height),(xoffset-.125,(idx+1)*-1*rec_height)),depth=-3,opacity=1,fillColor='Red',lineColor='Red')
                recs.append(rec)
    return recs
# Initialize components for Routine "pretrigger_instr"
pretrigger_instrClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Instructions:\n\nYou will be seeing series of images for this part of the experiment.\n\nEach image will be a blend of two different images. \n\nFor these blended images, you will be asked to focus on one of the layers.\n\nThe image layer that you should be focusing will be printed on the top portion of the screen. \n\nYou will also be receiving feedback on your ability to attend after each block. If the bar is green, you have done well. \n\nIf there are no images, please focus on the cross (+),  which will be located in the middle of the screen. \n\nExperimenter press spacebar to continue ',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
trigger_text = visual.TextStim(win=win, ori=0, name='trigger_text',
    text=u'Waiting for Scanner Trigger',    font=u'Arial',
    pos=[0, 0], height=.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
# Initialize components for Routine "baseline"
baselineClock = core.Clock()
image_4 = visual.ImageStim(win=win, name='image_4',
    image='stimulus/fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[1,1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

from scripts.feedback import ThermBase
import numpy as np

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instr = visual.TextStim(win=win, ori=0, name='instr',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "Transition"
TransitionClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=0,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stimulus"
stimulusClock = core.Clock()
face_image = visual.PatchStim(win=win, name='face_image',
    tex='sin', mask=None,
    ori=0, pos=[0, 0], size=[1,1], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=.5,
    texRes=128, interpolate=True, depth=0.0)
scene_image = visual.ImageStim(win=win, name='scene_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=1.0)
stimulus_instr = visual.TextStim(win=win, ori=0, name='stimulus_instr',
    text='nonsense',    font='Arial',
    pos=[0,.70 ], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image='stimulus/fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[1,1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
patch_2 = visual.PatchStim(win=win, name='patch_2',
    tex='sin', mask=None,
    ori=0, pos=[0, 0.75], size=[0.25, 0.25], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=0.0)
top_condition='face'
bottom_condition='scenes'
background_bar = visual.ShapeStim(win=win, name='background_bar', lineWidth=2.0, lineColor=(1.0,1.0,1.0), lineColorSpace='rgb',
pos=(0,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,-.5),(.125,-.5),(.125,.5),(-.125,.5)))#, fillColor='white', fillColorSpace='rgb')
zero_val_line=visual.ShapeStim(win=win, name='zero_val_line', lineWidth=2.0, lineColor=(1.0,1.0,1.0),lineColorSpace='rgb',
pos=(0,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,0),(.125,0)))
zero=visual.TextStim(win,text='0',font='', pos=(.155,0),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
top_text=visual.TextStim(win,text='placeholder',pos=(.275,.5),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
bottom_text=visual.TextStim(win,text='placeholder',pos=(.275,-.5),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
top_star = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[.5, .5], height=0.5, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
bottom_star = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[.5, -.5], height=0.5, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
image_3 = visual.ImageStim(win=win, name='image_3',
    image='stimulus/fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[1,1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

#Initialize compoennts for Routine "summary screen"
background_bar1 = visual.ShapeStim(win=win, name='background_bar', lineWidth=2.0, lineColor=(1.0,1.0,1.0), lineColorSpace='rgb',
pos=(-.6,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,-.5),(.125,-.5),(.125,.5),(-.125,.5)))#, fillColor='white', fillColorSpace='rgb')
zero_val_line1=visual.ShapeStim(win=win, name='zero_val_line', lineWidth=2.0, lineColor=(1.0,1.0,1.0),lineColorSpace='rgb',
pos=(-.6,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,0),(.125,0)))
zero1=visual.TextStim(win,text='0',font='', pos=(.155,0),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
top_text1=visual.TextStim(win,text='faces',pos=(.8,.6),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
bottom_text1=visual.TextStim(win,text='scenes',pos=(.8,-.6),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
top_star1 = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[-.6, .55], height=0.2, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
bottom_star1 = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[-.6, -.6], height=0.2, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
background_bar2 = visual.ShapeStim(win=win, name='background_bar', lineWidth=2.0, lineColor=(1.0,1.0,1.0), lineColorSpace='rgb',
pos=(-.2,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,-.5),(.125,-.5),(.125,.5),(-.125,.5)))#, fillColor='white', fillColorSpace='rgb')
zero_val_line2=visual.ShapeStim(win=win, name='zero_val_line', lineWidth=2.0, lineColor=(1.0,1.0,1.0),lineColorSpace='rgb',
pos=(-.2,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,0),(.125,0)))
top_star2 = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[-.2, .55], height=0.2, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
bottom_star2 = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[-.2, -.6], height=0.2, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
background_bar3 = visual.ShapeStim(win=win, name='background_bar', lineWidth=2.0, lineColor=(1.0,1.0,1.0), lineColorSpace='rgb',
pos=(.2,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,-.5),(.125,-.5),(.125,.5),(-.125,.5)))#, fillColor='white', fillColorSpace='rgb')
zero_val_line3=visual.ShapeStim(win=win, name='zero_val_line', lineWidth=2.0, lineColor=(1.0,1.0,1.0),lineColorSpace='rgb',
pos=(.2,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,0),(.125,0)))
top_star3 = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[.2, .55], height=0.2, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
bottom_star3 = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[.2, -.6], height=0.2, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
background_bar4 = visual.ShapeStim(win=win, name='background_bar', lineWidth=2.0, lineColor=(1.0,1.0,1.0), lineColorSpace='rgb',
pos=(.6,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,-.5),(.125,-.5),(.125,.5),(-.125,.5)))#, fillColor='white', fillColorSpace='rgb')
zero_val_line4=visual.ShapeStim(win=win, name='zero_val_line', lineWidth=2.0, lineColor=(1.0,1.0,1.0),lineColorSpace='rgb',
pos=(.6,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,0),(.125,0)))
zero4=visual.TextStim(win,text='0',font='', pos=(.6+.155,0),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
top_star4 = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[.6, .55], height=0.2, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
bottom_star4 = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[.6, -.6], height=0.2, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
    # Initialize components for Routine "ending_screen"
ending_screenClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='# of good feedback trials: %s \n \n # of badfeedback trials: %s'%(goodfeedback, badfeedback),    font=u'Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "pretrigger_instr"-------
t = 0
pretrigger_instrClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
pretrigger_instrComponents = []
pretrigger_instrComponents.append(text_2)
pretrigger_instrComponents.append(key_resp_4)
for thisComponent in pretrigger_instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pretrigger_instr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pretrigger_instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pretrigger_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pretrigger_instr"-------
for thisComponent in pretrigger_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trigger_loop = data.TrialHandler(nReps=num_triggers, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trigger_loop')
thisExp.addLoop(trigger_loop)  # add the loop to the experiment
thisTrigger_loop = trigger_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrigger_loop.rgb)
if thisTrigger_loop != None:
    for paramName in thisTrigger_loop.keys():
        exec(paramName + '= thisTrigger_loop.' + paramName)

for thisTrigger_loop in trigger_loop:
    currentLoop = trigger_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrigger_loop.rgb)
    if thisTrigger_loop != None:
        for paramName in thisTrigger_loop.keys():
            exec(paramName + '= thisTrigger_loop.' + paramName)
    
    #------Prepare to start Routine "trigger"-------
    t = 0
    triggerClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    trigger_button = event.BuilderKeyResponse()  # create an object of type KeyResponse
    trigger_button.status = NOT_STARTED
    # keep track of which components have finished
    triggerComponents = []
    triggerComponents.append(trigger_text)
    triggerComponents.append(trigger_button)
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trigger"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = triggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trigger_text* updates
        if t >= 0.0 and trigger_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            trigger_text.tStart = t  # underestimates by a little under one frame
            trigger_text.frameNStart = frameN  # exact frame index
            trigger_text.setAutoDraw(True)
        
        # *trigger_button* updates
        if t >= 0.0 and trigger_button.status == NOT_STARTED:
            # keep track of start time/frame for later
            trigger_button.tStart = t  # underestimates by a little under one frame
            trigger_button.frameNStart = frameN  # exact frame index
            trigger_button.status = STARTED
            # keyboard checking is just starting
            trigger_button.clock.reset()  # now t=0
            event.clearEvents()
        if trigger_button.status == STARTED:
            theseKeys = event.getKeys(keyList=['equal'])
            if len(theseKeys) > 0:  # at least one key was pressed
                trigger_button.keys = theseKeys[-1]  # just the last key pressed
                trigger_button.rt = trigger_button.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in triggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trigger"-------
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(trigger_button.keys) == 0:  # No response was made
       trigger_button.keys=None
    # store data for trigger_loop (TrialHandler)
    trigger_loop.addData('trigger_button.keys',trigger_button.keys)
    if trigger_button.keys != None:  # we had a response
        trigger_loop.addData('trigger_button.rt', trigger_button.rt)
    thisExp.nextEntry()
#------Prepare to start Routine "baseline"-------
t = 0
baselineClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
# keep track of which components have finished
baselineComponents = []
baselineComponents.append(image_4)
for thisComponent in baselineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "baseline"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = baselineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if t >= 0.0 and image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_4.tStart = t  # underestimates by a little under one frame
        image_4.frameNStart = frameN  # exact frame index
        image_4.setAutoDraw(True)
    elif image_4.status == STARTED and t >= (0.0 + timings['baseline']):
        image_4.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "baseline"-------
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None, trialList=data.importConditions(u'conditions/fouse_conditions_frun%s.csv'%(expInfo['session'])),
    name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)
image_list=0
for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "instruction"-------
    t = 0
    instructionClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    instr.setText(instruction_text)
    
    # keep track of which components have finished
    instructionComponents = []
    instructionComponents.append(instr)
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instruction"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        #murfi.update()
        # get current time
        t = instructionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr* updates
        if t >= 0.0 and instr.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr.tStart = t  # underestimates by a little under one frame
            instr.frameNStart = frameN  # exact frame index
            instr.setAutoDraw(True)
        elif instr.status == STARTED and t >= (0.0 + 2.0):
            instr.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockcount=0
    
    # set up handler to look after randomisation of conditions etc
    face_loop = data.TrialHandler(nReps=1, method=u'random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('conditions/fouse_stimuli_facelist.csv'),
        seed=((int(image_list)+5*int(expInfo['session']))), name='face_loop')
    thisExp.addLoop(face_loop)  # add the loop to the experiment
    thisFace_loop = face_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisFace_loop.rgb)
    if thisFace_loop != None:
        for paramName in thisFace_loop.keys():
            exec(paramName + '= thisFace_loop.' + paramName)
    
    for thisFace_loop in face_loop:
        currentLoop = face_loop
        # abbreviate parameter names if possible (e.g. rgb = thisFace_loop.rgb)
        if thisFace_loop != None:
            for paramName in thisFace_loop.keys():
                exec(paramName + '= thisFace_loop.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        scene_loop = data.TrialHandler(nReps=1, method=u'random', 
            extraInfo=expInfo, originPath=None,
            trialList=data.importConditions('conditions/fouse_stimuli_scenelist.csv'),
            seed=((int(image_list)+5*int(expInfo['session']))), name='scene_loop')
        thisExp.addLoop(scene_loop)  # add the loop to the experiment
        thisScene_loop = scene_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisScene_loop.rgb)
        if thisScene_loop != None:
            for paramName in thisScene_loop.keys():
                exec(paramName + '= thisScene_loop.' + paramName)
        
        for thisScene_loop in scene_loop:
            thisFace_loop=face_loop.next()
            currentLoop = scene_loop
            # abbreviate parameter names if possible (e.g. rgb = thisScene_loop.rgb)
            if thisScene_loop != None:
                for paramName in thisScene_loop.keys():
                    exec(paramName + '= thisScene_loop.' + paramName)
            if thisFace_loop != None:
                for paramName in thisFace_loop.keys():
                    exec(paramName + '= thisFace_loop.' + paramName)
            #------Prepare to start Routine "Transition"-------
            t = 0
            TransitionClock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            TransitionComponents = []
            TransitionComponents.append(image)
            for thisComponent in TransitionComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "Transition"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = TransitionClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image* updates
                if t >= 0.0 and image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image.tStart = t  # underestimates by a little under one frame
                    image.frameNStart = frameN  # exact frame index
                    image.setAutoDraw(True)
                elif image.status == STARTED and t >= (0.0 + .5):
                    image.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested that we end
                    routineTimer.reset()  # this is the new t0 for non-slip Routines
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TransitionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "Transition"-------
            for thisComponent in TransitionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            #------Prepare to start Routine "stimulus"-------
            t = 0
            stimulusClock.reset()  # clock 
            frameN = -1
            routineTimer.add(11.500000)
            # update component parameters for each repeat
            face_image.setTex(face)
            scene_image.setImage(scene)
            stimulus_instr.setText(instruction_text)
            blockcount= blockcount+1
            # keep track of which components have finished
            stimulusComponents = []
            stimulusComponents.append(face_image)
            stimulusComponents.append(scene_image)
            stimulusComponents.append(stimulus_instr)
            for thisComponent in stimulusComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "stimulus"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                #murfi.update()
                # get current time
                t = stimulusClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *face_image* updates
                if t >= 0.0 and face_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    face_image.tStart = t  # underestimates by a little under one frame
                    face_image.frameNStart = frameN  # exact frame index
                    face_image.setAutoDraw(True)
                elif face_image.status == STARTED and t >= (0.0 + timings['stimulus']):
                    face_image.setAutoDraw(False)
                
                # *scene_image* updates
                if t >= 0.0 and scene_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    scene_image.tStart = t  # underestimates by a little under one frame
                    scene_image.frameNStart = frameN  # exact frame index
                    scene_image.setAutoDraw(True)
                elif scene_image.status == STARTED and t >= (0.0 + timings['stimulus']):
                    scene_image.setAutoDraw(False)
                # *stimulus_instr* updates
                
                if t >= 0.0 and stimulus_instr.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stimulus_instr.tStart = t  # underestimates by a little under one frame
                    stimulus_instr.frameNStart = frameN  # exact frame index
                    stimulus_instr.setAutoDraw(True)
                elif stimulus_instr.status == STARTED and t >= (0.0 + timings['stimulus']):
                    stimulus_instr.setAutoDraw(False)
                    
                # check if all components have finished
                if not continueRoutine:  # a component has requested that we end
                    routineTimer.reset()  # this is the new t0 for non-slip Routines
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stimulusComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "stimulus"-------
            face_loop.next()
            for thisComponent in stimulusComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            if blockcount==3:
                face_loop.finished=1
                scene_loop.finished=1
            thisExp.nextEntry()
            
        # completed 1 repeats of 'scene_loop'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'face_loop'
    
    
    #------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = []
    fixationComponents.append(image_2)
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixation"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        #murfi.update()
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        elif image_2.status == STARTED and t >= (0.0 + timings['fixation']):
            image_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "feedback"-------
    t = 0
  
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(patch_2)
    feedbackComponents.append(background_bar)
    feedbackComponents.append(zero_val_line)
    feedbackComponents.append(zero)
    feedbackComponents.append(top_text)
    feedbackComponents.append(bottom_text)
    feedbackComponents.append(recs)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    image_list=image_list+1
    parts=thisTrial.instruction_text.split()
    if parts[2]=='Faces':
        top_text.setText('Faces')
        bottom_text.setText('Scenes')
        face_scene_conditions.append('Faces')
        feedbackComponents.append(top_star)
    elif parts[2]=='Scenes':
        top_text.setText('Faces')
        bottom_text.setText('Scenes')
        face_scene_conditions.append('Scenes')
        feedbackComponents.append(bottom_star)
    feedbackClock.reset()  # clock 
    frameN = 0
    routineTimer.add(4.000000)
    murfi.update()
    # update component parameters for each repeat
    patch_2.setOpacity(0)
    patch_2.setTex('stimulus/fixation.png')
    if thisTrial.instruction_text=='Attend to Scenes':
        top_text.setText('Faces')
        bottom_text.setText('Scenes')
        feedbackComponents.append('bottom_star')
        #max=float(expInfo['V2:scenes'])
        #min=float(expInfo['V1:faces'])
        max=float(expInfo['V1:faces'])
        min=float(expInfo['V2:scenes'])
        zero_val=float(expInfo['V4:50/50scenes'])
        index1= int(vector_indices[image_list-1][0])
        index2= int(vector_indices[image_list-1][1])
        FFA_vector=np.array(murfi.FB_FFA[index1:index2])
        PPA_vector=np.array(murfi.FB_PPA[index1:index2])
        indices_to_remove=[]
        for idx,val in enumerate(FFA_vector):
            if math.isnan(FFA_vector[idx]) or math.isnan(PPA_vector[idx]):
                indices_to_remove.append(idx)
        FFA_vector=np.delete(FFA_vector,indices_to_remove)
        PPA_vector=np.delete(PPA_vector,indices_to_remove)
        fb_average=np.median(np.array(FFA_vector)-np.array(PPA_vector))
        fb_average=np.median(np.array(FFA_vector)-np.array(PPA_vector))
        if fb_average >=zero_val:
            badfeedback=badfeedback+1
        elif fb_average <zero_val:
            goodfeedback=goodfeedback+1
    elif thisTrial.instruction_text =='Attend to Faces':
        top_text.setText('Faces')
        bottom_text.setText('Scenes')
        max=float(expInfo['V1:faces'])
        min=float(expInfo['V2:scenes'])
        zero_val=float(expInfo['V3:50/50faces'])
        feedbackComponents.append('top_star')
        index1= int(vector_indices[image_list-1][0])
        index2= int(vector_indices[image_list-1][1])
        FFA_vector=np.array(murfi.FB_FFA[index1:index2])
        PPA_vector=np.array(murfi.FB_PPA[index1:index2])
        indices_to_remove=[]
        for idx,val in enumerate(FFA_vector):
            if math.isnan(FFA_vector[idx]) or math.isnan(PPA_vector[idx]):
                indices_to_remove.append(idx)
        FFA_vector=np.delete(FFA_vector,indices_to_remove)
        PPA_vector=np.delete(PPA_vector,indices_to_remove)
        fb_average=np.median(np.array(FFA_vector)-np.array(PPA_vector))
        if fb_average <zero_val:
            badfeedback=badfeedback+1
        elif fb_average >=zero_val:
            goodfeedback=goodfeedback+1
    fb=[]
    if fb_average > max:
       fb = max
    elif fb_average< min:
       fb = min
    else:
       fb = fb_average
    fbs.append(fb)
    print thisTrial.instruction_text
    print 'feedback is %s'%fb_average
    print 'zero_val is %s'%zero_val
    print 'max is %s'%max
    print 'min is %s'%min
    rec=[]
    recs=[]
    rec=makeFBrecs(zero_val,fb,fillColor=None)
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

            
        # *patch_2* updates
        if t >= 0.0 and patch_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            patch_2.tStart = t  # underestimates by a little under one frame
            patch_2.frameNStart = frameN  # exact frame index
            patch_2.setAutoDraw(True)
            background_bar.setAutoDraw(True)
            zero_val_line.setAutoDraw(True)
            zero.setAutoDraw(True)
            top_text.setAutoDraw(True)
            bottom_text.setAutoDraw(True)
            if thisTrial.instruction_text=='Attend to Scenes':
                bottom_star.setAutoDraw(True)
            elif thisTrial.instruction_text=='Attend to Faces':
                top_star.setAutoDraw(True)
            
        #elif patch_2.status == STARTED and t >= (0.0 + 4):
        elif t >=(0.0+4):
            patch_2.setAutoDraw(False)
            background_bar.setAutoDraw(False)
            zero_val_line.setAutoDraw(False)
            zero.setAutoDraw(False)
            bottom_text.setAutoDraw(False)
            top_text.setAutoDraw(False)
            try:
                bottom_star.setAutoDraw(False)
                top_star.setAutoDraw(False)
            except:
                continue
#            if thisTrial.instruction_text=='Attend to Scenes':
#                bottom_star.setAutoDraw(False)
#            elif thisTrial.instruction_text=='Attend to Faces':
#                top_star.setAutoDraw(False)
        if frameN>=30:
            max_idx=30
        else:
            max_idx=floor(frameN)
        
        if int(max_idx)>1:
            for idx in range(int(max_idx)):
                recs[idx].setAutoDraw(True)
       # therm_ave= ThermBase(win, [0.25,1],[-0.125,-0.5])
        #t.plot(fb_,th_,arrow,frameN)
        #therm_ave.plot(fb,zero_val,frameN)
        #def plot(self,fb,zero_val,arrow='up',frame=20,maxframe=10):
        #therm_ave.draw()
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen

            win.flip()
    for idx in range(30):
        recs[idx].setAutoDraw(False)
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "fixation_2"-------
    t = 0
    fixation_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = []
    fixation_2Components.append(image_3)
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixation_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        #murfi.update()
        # get current time
        t = fixation_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        elif image_3.status == STARTED and t >= (0+timings['fixation_2']):
            image_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    #print image_list
    #-------Ending Routine "fixation_2"-------
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
#------Prepare to start Routine "ending_screen"-------
t = 0
ending_screenClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
ending_screenComponents = []
text.setText('# of successful feedback trials: %s \n \n# of unsuccessful feedback trials: %s\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Experimenter press space'%(goodfeedback, badfeedback))
ending_screenComponents.append(text)
for thisComponent in ending_screenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#------Prepare to start Routine "ending_screen"-------
t = 0
ending_screenClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ending_button = event.BuilderKeyResponse()  # create an object of type KeyResponse
ending_button.status = NOT_STARTED
# keep track of which components have finished
ending_screenComponents = []
ending_screenComponents.append(text)
ending_screenComponents.append(ending_button)
ending_screenComponents.append(background_bar1)
ending_screenComponents.append(zero_val_line1)
ending_screenComponents.append(top_text1)
ending_screenComponents.append(bottom_text1)
ending_screenComponents.append(background_bar2)
ending_screenComponents.append(zero_val_line2)
ending_screenComponents.append(background_bar3)
ending_screenComponents.append(zero_val_line3)
ending_screenComponents.append(background_bar4)
ending_screenComponents.append(zero_val_line4)
print face_scene_conditions
rec=[]
recs=[]
xoffsets=[-.6,-.2,.2,.6]
for idx in range(len(face_scene_conditions)):
    if face_scene_conditions[idx]=='Faces':
        ending_screenComponents.append(eval('top_star%s'%(int(idx)+1)))
        zero_val=float(expInfo['V3:50/50faces'])
        thisTrial.instruction_text='Attend to Faces'
        rec.append(makeFBrecs(zero_val,fbs[idx],fillColor=None,xoffset=xoffsets[idx]))
    elif face_scene_conditions[idx]=='Scenes':
        ending_screenComponents.append(eval('bottom_star%s'%(int(idx)+1)))
        zero_val=float(expInfo['V4:50/50scenes'])
        thisTrial.instruction_text='Attend to Scenes'
        rec.append(makeFBrecs(zero_val,fbs[idx],fillColor=None,xoffset=xoffsets[idx]))
ending_screenComponents.append(recs)
for thisComponent in ending_screenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ending_screen"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ending_screenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        #text.setAutoDraw(True)
        for thisComponent in ending_screenComponents:
            if hasattr(thisComponent, "setAutoDraw"): 
                thisComponent.setAutoDraw(True)
    if t >= 0.0 and ending_button.status == NOT_STARTED:
        # keep track of start time/frame for later
        ending_button.tStart = t  # underestimates by a little under one frame
        ending_button.frameNStart = frameN  # exact frame index
        ending_button.status = STARTED
        # keyboard checking is just starting
        ending_button.clock.reset()  # now t=0
        event.clearEvents()
    if ending_button.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            ending_button.keys = theseKeys[-1]  # just the last key pressed
            ending_button.rt = ending_button.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    for idx in range(len(recs)):
        recs[idx].setAutoDraw(True)
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ending_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ending_screen"-------
for thisComponent in ending_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()

# completed 5 repeats of 'trials'
print fbs
print 'FFA vector is'
print murfi.FB_FFA
print 'PPA vector is'
print murfi.FB_PPA
print '# of positive feedback trials is %s'%goodfeedback
print '# of bad feedback trials is %s'%badfeedback
murfi.update()
murfi_file=open('data' + os.path.sep + 'subject%s_session%s_%s_%s_%s.txt' %(expInfo['participant'], expInfo['session'], expInfo['date'],expName,'FFA_PPA'),'w+r')
for idx in range(len(murfi.FB_FFA)):
    murfi_file.write('%s %s %s \n'%(idx, murfi.FB_FFA[idx],murfi.FB_PPA[idx]))
murfi_file.close()
value_file=open('data'+ os.path.sep + 'baseline_values' + os.path.sep+'subject%s_session%s_%s_%s_%s.txt' %(expInfo['participant'], expInfo['session'], expInfo['date'],expName,'baseline_values'),'w+r')
value_file.write('%s \n %s \n %s \n %s \n'%(expInfo['V1:faces'],expInfo['V2:scenes'],expInfo['V3:50/50faces'],expInfo['V4:50/50scenes']))
value_file.close()

core.quit()
