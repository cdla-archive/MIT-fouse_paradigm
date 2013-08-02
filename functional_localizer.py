#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.76.00), Thu Jul 18 16:39:23 2013
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
from scripts.query_murfi import Murfi

murfi_IP = '192.168.2.5'
murfi_PORT = 15001
murfi_TR = 127

num_triggers=5
# Store info about the experiment session
expName = 'functional_localizer'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
timings={}

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
if expInfo['participant']=='debug' or expInfo['participant']=='debugtiming':
    filename = 'data' + os.path.sep +'debug' + os.path.sep +  '%s_%s_%s' %(expInfo['participant'], expInfo['date'],expName)
else:
    filename = 'data' + os.path.sep + '%s_%s_%s' %(expInfo['participant'], expInfo['date'],expName)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
if expInfo['participant']=='debug':
    win = visual.Window(size=(800,600), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
    timings['fixation']=1
    blockend=12
    print "**********DEBUG MODE************"
elif expInfo['participant']=='debugtiming':
    win=win = visual.Window(size=(800,600), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
    timings['fixation']=36
    print "**********DEBUG MODE with proper timings************"
    murfi_FAKE = True
    blockend=48
else:
    win = visual.Window(size=(1024,768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
    timings['fixation']=36
    blockend=48
    


# Initialize components for Routine "pretrigger_instr"
pretrigger_instrClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Instructions:\n\nIn this part of the experiment, you will be viewing either pure faces, pure scenes, or 50/50 blends of both. \n\n While viewing the images, if you see the same image twice in a row, please press the button box \n\n\n During the blends, if there is a repeat of the image of the condition that you are instructed please press the button box \n\n Experimenter press space to continue',    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
trigger_text = visual.TextStim(win=win, ori=0, name='trigger_text',
    text=u'Waiting for Scanner Trigger',    font=u'Arial',
    pos=[0, 0], height=.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
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
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

secondary_image = visual.ImageStim(win=win, name='secondary_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=.5,
    texRes=128, interpolate=True, depth=-2.0)
    
stimulus_instr = visual.TextStim(win=win, ori=0, name='stimulus_instr',
    text='nonsense',    font='Arial',
    pos=[0,.70 ], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
    # Initialize components for Routine "ending_screen"
ending_screenClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='placeholder',    font=u'Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
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

#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(timings['fixation'])
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
    elif fixation_image.status == STARTED and t >= (0.0 + timings['fixation']):#find me
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
image_list=0
trial_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
trial_resp.status=NOT_STARTED
# set up handler to look after randomisation of conditions etc
stimulus_type = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
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
    if thisStimulus_type.conditions =='Attend to face' or thisStimulus_type.conditions =='Attend to scene' or thisStimulus_type.conditions =='Scenes' or thisStimulus_type.conditions =='Faces':
        primary_image = visual.ImageStim(win=win, name='primary_image',
                image='sin', mask=None,
                ori=0, pos=[0, 0], size=[1, 1],
                color=[1,1,1], colorSpace='rgb', opacity=0.5,
                texRes=128, interpolate=True, depth=0.0)
            
        secondary_image = visual.ImageStim(win=win, name='secondary_image',
                image='sin', mask=None,
                ori=0, pos=[0, 0], size=[1,1],
                color=[1,1,1], colorSpace='rgb', opacity=.5,
                texRes=128, interpolate=True, depth=0)
    
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
            elif instr.status == STARTED and t >= (0.0 + 2):
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
    image_list=image_list+1
        #-------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockcount=0
    if thisStimulus_type.conditions=='fixation':
        primary_image = visual.ImageStim(win=win, name='primary_image',
        image=u'stimulus/fixation.png', mask=None,
        ori=0, pos=[0, 0], size=[1,1],
        color=[1,1,1], colorSpace=u'rgb', opacity=1,
        texRes=128, interpolate=True, depth=0.0)
            
        secondary_image = visual.ImageStim(win=win, name='secondary_image',
        image=u'stimulus/fixation.png', mask=None,
        ori=0, pos=[0, 0], size=[1,1],
        color=[1,1,1], colorSpace=u'rgb', opacity=0,
        texRes=128, interpolate=True, depth=1.0)
    # set up handler to look after randomisation of conditions etc
    print thisStimulus_type.conditions
    print image_list
    #print int(expInfo['session'])
    #print image_list
    primary_stimlist = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('conditions/functional_localizer/fouse_run%s_block%s.csv'%(expInfo['session'],image_list)),
        name='primary_stimlist')
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
        #------Prepare to start Routine "fixation_2"-------
        t = 0
        fixation_2Clock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixation_2Components = []
        fixation_2Components.append(fixation_image_2)
        stimulus_instr.setText(instruction_text)
        if thisStimulus_type.conditions=='Attend to scene' or thisStimulus_type.conditions=='Attend to face' or thisStimulus_type.conditions=='Faces' or thisStimulus_type.conditions=='Scenes':
            fixation_2Components.append(stimulus_instr)
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
            if thisStimulus_type.conditions=='Attend to scene' or thisStimulus_type.conditions=='Attend to face' or thisStimulus_type.conditions=='Faces' or thisStimulus_type.conditions=='Scenes':
                               # *stimulus_instr* updates
                if t >= 0.0 and stimulus_instr.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stimulus_instr.tStart = t  # underestimates by a little under one frame
                    stimulus_instr.frameNStart = frameN  # exact frame index
                    stimulus_instr.setAutoDraw(True)
            elif stimulus_instr.status == STARTED and t >= (0.0 + 0.25):
                    stimulus_instr.setAutoDraw(False)
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
        theseKeys=[]
        if thisStimulus_type.conditions=='Faces':
            primary_image.setImage('stimulus/Faces/face0%02d.jpg'%(int(face)))
            secondary_image.setImage('stimulus/Scenes/scene%02d.jpg'%(int(scene)))
            primary_image.setOpacity(1)
            secondary_image.setOpacity(0)
            stimulus_instr.setText(instruction_text)
        elif thisStimulus_type.conditions=='Scenes':
            primary_image.setImage('stimulus/Faces/face0%02d.jpg'%(int(face)))
            secondary_image.setImage('stimulus/Scenes/scene%02d.jpg'%(int(scene)))
            primary_image.setOpacity(0)
            secondary_image.setOpacity(1)
            stimulus_instr.setText(instruction_text)
        elif thisStimulus_type.conditions=='fixation':
            primary_image.setImage('stimulus/fixation.png')
            secondary_image.setImage('stimulus/fixation.png')
            primary_image.setOpacity(1)
            primary_image.setDepth(0)
            secondary_image.setOpacity(0)
            secondary_image.setDepth(1)
        else:
            primary_image.setImage('stimulus/Faces/face0%02d.jpg'%(int(face)))
            secondary_image.setImage('stimulus/Scenes/scene%02d.jpg'%(int(scene)))
            primary_image.setOpacity(.5)
            secondary_image.setOpacity(1)
            primary_image.setDepth(0)
            secondary_image.setDepth(1)
            stimulus_instr.setText(instruction_text)
            
        
        # keep track of which components have finished
        blocksComponents = []
        blocksComponents.append(primary_image)
        blocksComponents.append(secondary_image)
        blocksComponents.append(trial_resp)
        if thisStimulus_type.conditions=='Attend to scene' or thisStimulus_type.conditions=='Attend to face' or thisStimulus_type.conditions=='Faces' or thisStimulus_type.conditions=='Scenes':
            blocksComponents.append(stimulus_instr)
        response_key=[]
        for thisComponent in blocksComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        event.clearEvents()
        trial_resp.keys=[]
        trial_resp.rt=[]
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
                secondary_image.setAutoDraw(False)
            if t >= 0.0 and secondary_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                secondary_image.tStart = t  # underestimates by a little under one frame
                secondary_image.frameNStart = frameN  # exact frame index
                secondary_image.setAutoDraw(True)
            elif secondary_image.status == STARTED and t >= (0.0 + .5):
                secondary_image.setAutoDraw(False)
            if thisStimulus_type.conditions=='Attend to scene' or thisStimulus_type.conditions=='Attend to face' or thisStimulus_type.conditions=='Faces' or thisStimulus_type.conditions=='Scenes':
                               # *stimulus_instr* updates
                if t >= 0.0 and stimulus_instr.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stimulus_instr.tStart = t  # underestimates by a little under one frame
                    stimulus_instr.frameNStart = frameN  # exact frame index
                    stimulus_instr.setAutoDraw(True)
                elif stimulus_instr.status == STARTED and t >= (0.0 + 0.5):
                    stimulus_instr.setAutoDraw(False)
            # *secondary_image* updates
               
        #*trial_resp* updates
            if t>=0 and trial_resp.status==NOT_STARTED:
                #keep track of start time/frame for later
                trial_resp.tStart=t#underestimates by a little under one frame
                trial_resp.frameNStart=frameN#exact frame index
                trial_resp.status=STARTED
                #keyboard checking is just starting
                trial_resp.clock.reset() # now t=0
            elif trial_resp.status==STARTED and t>=0+ .75:
                trial_resp.status=STOPPED
            if trial_resp.status==STARTED:#only update if being drawn
                theseKeys = event.getKeys()
            if len(theseKeys)>0:#at least one key was pressed
                    #trial_resp.keys=theseKeys[-1]#just the last key pressed   $$$$$$CHANGE THIS!!!!!!!!!$$$$$$$$
                trial_resp.keys.extend(theseKeys)
                trial_resp.rt = trial_resp.clock.getTime()
                    #if trialNum==0: runClock.reset()
                   # response_startTime = runClock.getTime()
                    #print response_startTime
            primary_stimlist.addData('response',trial_resp.keys)
            primary_stimlist.addData('response_time',trial_resp.rt)
            #primary_stimlist.addData('face_shown',primary_image)
            #primary_stimlist.addData('scene_shown',secondary_image)
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
        if blockcount==blockend:
            primary_stimlist.finished=1
            
        # completed 1 repeats of 'second_stimlist'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'primary_stimlist'
    
    thisExp.nextEntry()
#------Prepare to start Routine "ending_screen"-------
t = 0
ending_screenClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
ending_screenComponents = []
text.setText('          Good Job!!!! \n\n\n\n\n\n\n\n\n\n\n Experimenter press space')
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
    
# completed 1 repeats of 'stimulus_type'
#
#print murfi.FB_FFA
#print murfi.FB_PPA
#
#murfi_file=open('data' + os.path.sep + '%s_%s_%s_%s.txt' %(expInfo['participant'], expInfo['date'],expName,'FFA_PPA'),'w+r')
#for idx in range(len(murfi.FB_FFA)):
#    murfi_file.write('%s %s %s \n'%(idx, murfi.FB_FFA[idx],murfi.FB_PPA[idx]))
#murfi_file.close()



win.close()
core.quit()
