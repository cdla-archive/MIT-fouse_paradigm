#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.76.00), Thu Jul 18 18:16:24 2013
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'functional_localizer'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/Carlo/Dropbox/Fouse/Fouse_paradigm_071613/functional_localizer.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb')

# Initialize components for Routine "pretrigger_instr"
pretrigger_instrClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Instructions:\r\n\r\nPlease pay attention to the images',    font='Arial',
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

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_image = visual.ImageStim(win=win, name='fixation_image',
    image=u'stimulus/fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[1,1],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instr = visual.TextStim(win=win, ori=0, name='instr',
    text='nonsense',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
fixation_image_2 = visual.ImageStim(win=win, name='fixation_image_2',
    image=u'stimulus/fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[1,1],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blocks"
blocksClock = core.Clock()
primary_image = visual.ImageStim(win=win, name='primary_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    texRes=128, interpolate=True, depth=0.0)

secondary_image = visual.ImageStim(win=win, name='secondary_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)

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
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

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
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "trigger"-------
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(36.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fixation_image)
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
    
    # *fixation_image* updates
    if t >= 0.0 and fixation_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation_image.tStart = t  # underestimates by a little under one frame
        fixation_image.frameNStart = frameN  # exact frame index
        fixation_image.setAutoDraw(True)
    elif fixation_image.status == STARTED and t >= (0.0 + 36):
        fixation_image.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
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

# set up handler to look after randomisation of conditions etc
stimulus_type = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=u'/Users/Carlo/Dropbox/Fouse/Fouse_paradigm_071613/functional_localizer.psyexp',
    trialList=data.importConditions('conditions/functional_localizer_conditions.csv'),
    seed=None, name='stimulus_type')
thisExp.addLoop(stimulus_type)  # add the loop to the experiment
thisStimulus_type = stimulus_type.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisStimulus_type.rgb)
if thisStimulus_type != None:
    for paramName in thisStimulus_type.keys():
        exec(paramName + '= thisStimulus_type.' + paramName)

for thisStimulus_type in stimulus_type:
    currentLoop = stimulus_type
    # abbreviate parameter names if possible (e.g. rgb = thisStimulus_type.rgb)
    if thisStimulus_type != None:
        for paramName in thisStimulus_type.keys():
            exec(paramName + '= thisStimulus_type.' + paramName)
    
    #------Prepare to start Routine "instruction"-------
    t = 0
    instructionClock.reset()  # clock 
    frameN = -1
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
    while continueRoutine:
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
        elif instr.status == STARTED and t >= (0.0 + ins_placeholder):
            instr.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockcount=0
    
    # set up handler to look after randomisation of conditions etc
    primary_stimlist = data.TrialHandler(nReps=1, method=u'random', 
        extraInfo=expInfo, originPath=u'/Users/Carlo/Dropbox/Fouse/Fouse_paradigm_071613/functional_localizer.psyexp',
        trialList=data.importConditions('conditions/fouse_stimuli_facelist.csv'),
        seed=seed_holder, name='primary_stimlist')
    thisExp.addLoop(primary_stimlist)  # add the loop to the experiment
    thisPrimary_stimlist = primary_stimlist.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisPrimary_stimlist.rgb)
    if thisPrimary_stimlist != None:
        for paramName in thisPrimary_stimlist.keys():
            exec(paramName + '= thisPrimary_stimlist.' + paramName)
    
    for thisPrimary_stimlist in primary_stimlist:
        currentLoop = primary_stimlist
        # abbreviate parameter names if possible (e.g. rgb = thisPrimary_stimlist.rgb)
        if thisPrimary_stimlist != None:
            for paramName in thisPrimary_stimlist.keys():
                exec(paramName + '= thisPrimary_stimlist.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        second_stimlist = data.TrialHandler(nReps=1, method=u'random', 
            extraInfo=expInfo, originPath=u'/Users/Carlo/Dropbox/Fouse/Fouse_paradigm_071613/functional_localizer.psyexp',
            trialList=data.importConditions('conditions/fouse_stimuli_scenelist.csv'),
            seed=seed_placeholder, name='second_stimlist')
        thisExp.addLoop(second_stimlist)  # add the loop to the experiment
        thisSecond_stimlist = second_stimlist.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisSecond_stimlist.rgb)
        if thisSecond_stimlist != None:
            for paramName in thisSecond_stimlist.keys():
                exec(paramName + '= thisSecond_stimlist.' + paramName)
        
        for thisSecond_stimlist in second_stimlist:
            currentLoop = second_stimlist
            # abbreviate parameter names if possible (e.g. rgb = thisSecond_stimlist.rgb)
            if thisSecond_stimlist != None:
                for paramName in thisSecond_stimlist.keys():
                    exec(paramName + '= thisSecond_stimlist.' + paramName)
            
            #------Prepare to start Routine "fixation_2"-------
            t = 0
            fixation_2Clock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.250000)
            # update component parameters for each repeat
            # keep track of which components have finished
            fixation_2Components = []
            fixation_2Components.append(fixation_image_2)
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
                
                # *fixation_image_2* updates
                if t >= 0.0 and fixation_image_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fixation_image_2.tStart = t  # underestimates by a little under one frame
                    fixation_image_2.frameNStart = frameN  # exact frame index
                    fixation_image_2.setAutoDraw(True)
                elif fixation_image_2.status == STARTED and t >= (0.0 + .25):
                    fixation_image_2.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
            
            #------Prepare to start Routine "blocks"-------
            t = 0
            blocksClock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            primary_image.setImage(primary_placeholder)
            
            secondary_image.setImage(secondary_placeholder)
            # keep track of which components have finished
            blocksComponents = []
            blocksComponents.append(primary_image)
            blocksComponents.append(secondary_image)
            for thisComponent in blocksComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "blocks"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = blocksClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *primary_image* updates
                if t >= 0.0 and primary_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    primary_image.tStart = t  # underestimates by a little under one frame
                    primary_image.frameNStart = frameN  # exact frame index
                    primary_image.setAutoDraw(True)
                elif primary_image.status == STARTED and t >= (0.0 + .5):
                    primary_image.setAutoDraw(False)
                
                
                # *secondary_image* updates
                if t >= 0.0 and secondary_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    secondary_image.tStart = t  # underestimates by a little under one frame
                    secondary_image.frameNStart = frameN  # exact frame index
                    secondary_image.setAutoDraw(True)
                elif secondary_image.status == STARTED and t >= (0.0 + .5):
                    secondary_image.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blocksComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "blocks"-------
            for thisComponent in blocksComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            blockcount=blockcount+1
            if blockcount==48:
                primary_stimlist.finished=1
                second_stimlist.finished=1
            thisExp.nextEntry()
            
        # completed 1 repeats of 'second_stimlist'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'primary_stimlist'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'stimulus_type'



win.close()
core.quit()
