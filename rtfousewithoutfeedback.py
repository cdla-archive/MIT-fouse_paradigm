#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.76.00), Thu Jul 18 08:45:10 2013
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

murfi_IP = '192.168.2.5'
murfi_PORT = 15001
murfi_TR = 127
num_triggers=5

# Store info about the experiment session
expName = 'rtfousewithoutfeedback'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

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
    timings['baseline']=1
    timings['stimulus']=1
    timings['fixation']=1
    timings['fixation_2']=1
    print "**********DEBUG MODE************"
    murfi_FAKE = True
elif expInfo['participant']=='debugtiming':
    win=win = visual.Window(size=(1024,768), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
    timings['baseline']=30
    timings['stimulus']=11.5
    timings['fixation']=4
    timings['fixation_2']=10
    print "**********DEBUG MODE with proper timings************"
    murfi_FAKE = True
else:
    win = visual.Window(size=(1024,768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
    timings['baseline']=30
    timings['stimulus']=11.5
    timings['fixation']=4
    timings['fixation_2']=10
    murfi_FAKE = False

murfi = Murfi(murfi_IP, murfi_PORT, murfi_TR, murfi_FAKE)
# Initialize components for Routine "pretrigger_instr"
pretrigger_instrClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Instructions:\n\nYou will be seeing series of images for this part of the experiment.\n\nEach image will be a blend of two different images. \n\nFor these blended images, you will be asked to focus on one of the layers.\n\nThe image layer that you should be focusing will be printed on the top portion of the screen. \n\nFor example, If the task was to focus on face image layer of the blended image, there will be a text on top portion of the screen that says “attend to faces”.\n\nIf there are no images, please focus on the cross (+),  which will be located in the middle of the screen. \n\nExperimenter press spacebar to continue ',    font=u'Arial',
    pos=[0, 0], height=.06, wrapWidth=None,
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
scene_image = visual.ImageStim(win=win, name='scene_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=1)
face_image = visual.ImageStim(win=win, name='face_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1,1],
    color=[1,1,1], colorSpace='rgb', opacity=.5,
    texRes=128, interpolate=True, depth=0)

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

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image='stimulus/fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[1,1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
image_3 = visual.ImageStim(win=win, name='image_3',
    image='stimulus/fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[1,1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
# Initialize components for Routine "ending_screen"
ending_screenClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='placeholder',    font=u'Arial',
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

#------Prepare to start Routine "trigger"-------
t = 0
triggerClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
triggerComponents = []
triggerComponents.append(text)
triggerComponents.append(key_resp_2)
for thisComponent in triggerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

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
routineTimer.add(timings['baseline'])
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
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('conditions/fouse_conditions_nofrun%s.csv'%(expInfo['session'])),
    name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)
stimulus_count=0
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
    scene_loop = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('conditions/fouse_stimulus_nof_run00%s.csv'%int(expInfo['session'])), name='scene_loop')
    thisExp.addLoop(scene_loop)  # add the loop to the experiment
    thisScene_loop = scene_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisScene_loop.rgb)
    if thisScene_loop != None:
        for paramName in thisScene_loop.keys():
            exec(paramName + '= thisScene_loop.' + paramName)
    skipped=0
    while skipped<stimulus_count:
            scene_loop.next()
            skipped=skipped+1
    for thisScene_loop in scene_loop:

        currentLoop = scene_loop
        # abbreviate parameter names if possible (e.g. rgb = thisScene_loop.rgb)
        if thisScene_loop != None:
            for paramName in thisScene_loop.keys():
                exec(paramName + '= thisScene_loop.' + paramName)
        
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
        routineTimer.add(timings['stimulus'])
        # update component parameters for each repeat
        face_image.setImage(face)
        scene_image.setImage(scene)
        stimulus_instr.setText(instruction_text)
        blockcount= blockcount+1
        # keep track of which components have finished
        stimulusComponents = []
        stimulusComponents.append(scene_image)
        stimulusComponents.append(face_image)
        print face
        print scene
        stimulusComponents.append(stimulus_instr)
        for thisComponent in stimulusComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "stimulus"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimulusClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *scene_image* updates
                            # *face_image* updates
            if t >= 0.0 and face_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                face_image.tStart = t  # underestimates by a little under one frame
                face_image.frameNStart = frameN  # exact frame index
                face_image.setAutoDraw(True)
            elif face_image.status == STARTED and t >= (0.0 + timings['stimulus']):
                face_image.setAutoDraw(False)
            
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
        for thisComponent in stimulusComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if blockcount==3:
            scene_loop.finished=1
        stimulus_count=stimulus_count+1
        thisExp.nextEntry()
            
    
    #------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(timings['fixation'])
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
    
    #------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(timings['fixation'])
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
    murfi.update()
    #------Prepare to start Routine "fixation_2"-------
    t = 0
    fixation_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(timings['fixation_2'])
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
    
    #-------Ending Routine "fixation_2"-------
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            

    thisExp.nextEntry()
print murfi.FB_FFA
print murfi.FB_PPA

murfi_file=open('data' + os.path.sep + '%s_%s_%s_%s.txt' %(expInfo['participant'], expInfo['date'],expName,'FFA_PPA'),'w+r')

for idx in range(len(murfi.FB_FFA)):
    murfi_file.write('%s %s %s \n'%(idx, murfi.FB_FFA[idx],murfi.FB_PPA[idx]))
murfi_file.close()

#------Prepare to start Routine "ending_screen"-------
t = 0
ending_screenClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
ending_screenComponents = []
text.setText('           Good Job!!!! \n\n\n\n\n\n\n\n\n\n\n Experimenter press space')
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
        text.setAutoDraw(True)
    
    # *ending_button* updates
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
core.quit()
# completed 4 repeats of 'trials'

core.quit()
