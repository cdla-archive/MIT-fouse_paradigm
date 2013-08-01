#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.76.00), Sat Jul 20 14:23:49 2013
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

# Store info about the experiment session
expName = 'rtfousewithfeedback'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/cdla/Dropbox/Fouse/Fouse_paradigm_071613/old_exp_files/rtfousewithfeedback.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb')

# Initialize components for Routine "pretrigger_instr"
pretrigger_instrClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Instructions:\r\n\r\nYou will be presented with images blends of faces and scenes.\r\n\r\n- When instructed to attend to house, focus on the house image.\r\n\r\n- When instructed to attend to face, focus on the face image.\r\n\r\n- When instructed to passively view, do not focus on either face or house.\r\n\r\nDuring this run, you will receive feedback after each block on your ability to attend\r\nExperimenter press spacebar to continue ',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='Waiting for scanner trigger ...',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
image_4 = visual.ImageStim(win=win, name='image_4',
    image='stimulus/fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[2,2],
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
face_image = visual.PatchStim(win=win, name='face_image',
    tex='sin', mask=None,
    ori=0, pos=[0, 0], size=[1,1], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=.5,
    texRes=128, interpolate=True, depth=0.0)
scene_image = visual.ImageStim(win=win, name='scene_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=.5,
    texRes=128, interpolate=True, depth=-1.0)
text_5_fake = visual.TextStim(win=win, ori=0, name='text_5_fake',
    text='nonsense',    font='Arial',
    pos=[0, 1], height=0.0, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=0,
    depth=-2.0)


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
def extract(rt,dr,mask='active'):
    trials = np.asarray(rt.trial_type[mask])
    data = np.asarray(rt.data[mask])
    if (trials==dr).any():
        return data[trials==dr].tolist()
    else:
        return []


# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
image_3 = visual.ImageStim(win=win, name='image_3',
    image='stimulus/fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[1,1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_5_end = visual.TextStim(win=win, ori=0, name='text_5_end',
    text='Good Job!\n\nGet ready for the next run!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)


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

#-------Start Routine "trigger"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = triggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
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
    elif image_4.status == STARTED and t >= (0.0 + 30):
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
trials = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=u'/Users/cdla/Dropbox/Fouse/Fouse_paradigm_071613/old_exp_files/rtfousewithfeedback.psyexp',
    trialList=data.importConditions('conditions/fouse_conditions.csv'),
    seed=placeholder3, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

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
    face_loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=u'/Users/cdla/Dropbox/Fouse/Fouse_paradigm_071613/old_exp_files/rtfousewithfeedback.psyexp',
        trialList=data.importConditions('conditions/fouse_stimuli_facelist.xlsx'),
        seed=placeholder2, name='face_loop')
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
        scene_loop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=u'/Users/cdla/Dropbox/Fouse/Fouse_paradigm_071613/old_exp_files/rtfousewithfeedback.psyexp',
            trialList=data.importConditions('conditions/fouse_stimuli_scenelist.xlsx'),
            seed=placeholder1, name='scene_loop')
        thisExp.addLoop(scene_loop)  # add the loop to the experiment
        thisScene_loop = scene_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisScene_loop.rgb)
        if thisScene_loop != None:
            for paramName in thisScene_loop.keys():
                exec(paramName + '= thisScene_loop.' + paramName)
        
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
            routineTimer.add(11.500000)
            # update component parameters for each repeat
            face_image.setTex(face)
            scene_image.setImage(scene)
            text_5_fake.setText(face)
            blockcount= blockcount+1
            print scene
            print face
            # keep track of which components have finished
            stimulusComponents = []
            stimulusComponents.append(face_image)
            stimulusComponents.append(scene_image)
            stimulusComponents.append(text_5_fake)
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
                
                # *face_image* updates
                if t >= 0.0 and face_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    face_image.tStart = t  # underestimates by a little under one frame
                    face_image.frameNStart = frameN  # exact frame index
                    face_image.setAutoDraw(True)
                elif face_image.status == STARTED and t >= (0.0 + 11.5):
                    face_image.setAutoDraw(False)
                
                # *scene_image* updates
                if t >= 0.0 and scene_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    scene_image.tStart = t  # underestimates by a little under one frame
                    scene_image.frameNStart = frameN  # exact frame index
                    scene_image.setAutoDraw(True)
                elif scene_image.status == STARTED and t >= (0.0 + 11.5):
                    scene_image.setAutoDraw(False)
                
                # *text_5_fake* updates
                if t >= 0.0 and text_5_fake.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_5_fake.tStart = t  # underestimates by a little under one frame
                    text_5_fake.frameNStart = frameN  # exact frame index
                    text_5_fake.setAutoDraw(True)
                elif text_5_fake.status == STARTED and t >= (0.0 + 0.0):
                    text_5_fake.setAutoDraw(False)
                
                
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
            for idx,i in enumerate(scene_loop.trialList):
                     name=str(scene_loop.trialList[idx])
                     if scene in name:
                         del scene_loop.trialList[idx]
            for idx,i in enumerate(face_loop.trialList):
                     name=str(face_loop.trialList[idx])
                     if face in name:
                         del face_loop.trialList[idx]
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
        elif image_2.status == STARTED and t >= (0.0 + 4):
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
    feedbackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    patch_2.setOpacity(1)
    patch_2.setTex(image)
    rtdata = rt.check(arrow)[0]
    fb = get_feedback(rt,arrow,7)
    Feedbacks[arrow].append(fb)
    
    if FB:
        th = get_target(Feedbacks,arrow)
    Targets[arrow].append(th)    
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(patch_2)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
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
        elif patch_2.status == STARTED and t >= (0.0 + 4):
            patch_2.setAutoDraw(False)
        t = ThermBase(win, [0.25,1],[-0.125,-0.5])
        if FB:
            t.plot(fb,th,arrow,frameN)
        t.draw()
        
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
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rt.check(arrow+'_fb')
    
    #------Prepare to start Routine "fixation_2"-------
    t = 0
    fixation_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(11.000000)
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
        if t >= 10 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        elif image_3.status == STARTED and t >= (10 + 1):
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
    
# completed 5 repeats of 'trials'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
text_6.setText(run_num)
rt.save(filename[:-5]+'_run_%s'%expInfo['session']+'.npz',Feedbacks,Targets)
rt.close()
# keep track of which components have finished
endComponents = []
endComponents.append(text_5_end)
endComponents.append(key_resp_3)
endComponents.append(text_6)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5_end* updates
    if t >= 0.0 and text_5_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5_end.tStart = t  # underestimates by a little under one frame
        text_5_end.frameNStart = frameN  # exact frame index
        text_5_end.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    elif text_6.status == STARTED and t >= (0.0 + 1.0):
        text_6.setAutoDraw(False)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)





win.close()
core.quit()
