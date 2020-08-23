#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on 八月 23, 2020, at 16:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'EDP_test'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\user\\Desktop\\TOM project\\EDP_program\\EDP_test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='EDP', color='lightgray', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text_ins = visual.TextStim(win=win, name='text_ins',
    text='Ready\n     \nClick OK to start\n',
    font='Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
OKbutton = visual.ImageStim(
    win=win,
    name='OKbutton', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "trial_1"
trial_1Clock = core.Clock()
interface_1 = visual.ImageStim(
    win=win,
    name='interface_1', 
    image='./interface/1.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_1 = visual.Slider(win=win, name='slider_1',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(-2000,0),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
ratingText_1 = visual.TextStim(win=win, name='ratingText_1',
    text=slider_1.markerPos,
    font='Arial',
    pos=(376.5, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
OKbutton_1 = visual.ImageStim(
    win=win,
    name='OKbutton_1', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
mouse_1 = event.Mouse(win=win)
x, y = [None, None]
mouse_1.mouseClock = core.Clock()

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
interface_2 = visual.ImageStim(
    win=win,
    name='interface_2', 
    image='./interface/2.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_2 = visual.Slider(win=win, name='slider_2',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(0, 2000),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
ratingText_2 = visual.TextStim(win=win, name='ratingText_2',
    text=slider_2.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
OKbutton_2 = visual.ImageStim(
    win=win,
    name='OKbutton_2', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "trial_3"
trial_3Clock = core.Clock()
interface_3 = visual.ImageStim(
    win=win,
    name='interface_3', 
    image='./interface/3.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_3 = visual.Slider(win=win, name='slider_3',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(-2000, 0),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_x1pos = visual.TextStim(win=win, name='text_x1pos',
    text=None,
    font='Arial',
    pos=(-155.3, 0), height=34, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ratingText_3 = visual.TextStim(win=win, name='ratingText_3',
    text=slider_3.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
OKbutton_3 = visual.ImageStim(
    win=win,
    name='OKbutton_3', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "trial_4"
trial_4Clock = core.Clock()
interface_4 = visual.ImageStim(
    win=win,
    name='interface_4', 
    image='./interface/4.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_4 = visual.Slider(win=win, name='slider_4',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(0, 2000),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_x2pos = visual.TextStim(win=win, name='text_x2pos',
    text=None,
    font='Arial',
    pos=(-155.3, 0), height=34, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ratingText_4 = visual.TextStim(win=win, name='ratingText_4',
    text=slider_4.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
OKbutton_4 = visual.ImageStim(
    win=win,
    name='OKbutton_4', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()

# Initialize components for Routine "trial_5"
trial_5Clock = core.Clock()
interface_5 = visual.ImageStim(
    win=win,
    name='interface_5', 
    image='./interface/5.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_5 = visual.Slider(win=win, name='slider_5',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(0, 2000),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_x1pos_2 = visual.TextStim(win=win, name='text_x1pos_2',
    text=None,
    font='Arial',
    pos=(-155.3, 151.6), height=34, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ratingText_5 = visual.TextStim(win=win, name='ratingText_5',
    text=slider_5.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
OKbutton_5 = visual.ImageStim(
    win=win,
    name='OKbutton_5', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()

# Initialize components for Routine "trial_6"
trial_6Clock = core.Clock()
interface_6 = visual.ImageStim(
    win=win,
    name='interface_6', 
    image='./interface/6.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_6 = visual.Slider(win=win, name='slider_6',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(0, 2000),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_x2posd = visual.TextStim(win=win, name='text_x2posd',
    text=None,
    font='Arial',
    pos=(-155.3, 151.6), height=34, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ratingText_6 = visual.TextStim(win=win, name='ratingText_6',
    text=slider_6.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
OKbutton_6 = visual.ImageStim(
    win=win,
    name='OKbutton_6', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()

# Initialize components for Routine "trial_7"
trial_7Clock = core.Clock()
interface_7 = visual.ImageStim(
    win=win,
    name='interface_7', 
    image='./interface/7.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_7 = visual.Slider(win=win, name='slider_7',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(0, 2000),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_L = visual.TextStim(win=win, name='text_L',
    text=None,
    font='Arial',
    pos=(-155.3, 0), height=34, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ratingText_7 = visual.TextStim(win=win, name='ratingText_7',
    text=slider_7.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
OKbutton_7 = visual.ImageStim(
    win=win,
    name='OKbutton_7', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()

# Initialize components for Routine "trial_8"
trial_8Clock = core.Clock()
interface_8 = visual.ImageStim(
    win=win,
    name='interface_8', 
    image='./interface/8.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_8 = visual.Slider(win=win, name='slider_8',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(0, 2000),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_x1neg = visual.TextStim(win=win, name='text_x1neg',
    text=None,
    font='Arial',
    pos=(-155.3, 0), height=34, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ratingText_8 = visual.TextStim(win=win, name='ratingText_8',
    text=slider_8.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
OKbutton_8 = visual.ImageStim(
    win=win,
    name='OKbutton_8', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()

# Initialize components for Routine "trial_9"
trial_9Clock = core.Clock()
interface_9 = visual.ImageStim(
    win=win,
    name='interface_9', 
    image='./interface/9.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_9 = visual.Slider(win=win, name='slider_9',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(0, 2000),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_x2neg = visual.TextStim(win=win, name='text_x2neg',
    text=None,
    font='Arial',
    pos=(-155.3, 0), height=34, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ratingText_9 = visual.TextStim(win=win, name='ratingText_9',
    text=slider_9.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
OKbutton_9 = visual.ImageStim(
    win=win,
    name='OKbutton_9', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()

# Initialize components for Routine "trial_10"
trial_10Clock = core.Clock()
interface_10 = visual.ImageStim(
    win=win,
    name='interface_10', 
    image='./interface/10.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_10 = visual.Slider(win=win, name='slider_10',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(0, 2000),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_x1neg_2 = visual.TextStim(win=win, name='text_x1neg_2',
    text=None,
    font='Arial',
    pos=(-155.3, 151.6), height=34, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_L_2 = visual.TextStim(win=win, name='text_L_2',
    text=None,
    font='Arial',
    pos=(-155.3, 0), height=34, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ratingText_10 = visual.TextStim(win=win, name='ratingText_10',
    text=slider_10.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
OKbutton_10 = visual.ImageStim(
    win=win,
    name='OKbutton_10', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()

# Initialize components for Routine "trial_11"
trial_11Clock = core.Clock()
interface_11 = visual.ImageStim(
    win=win,
    name='interface_11', 
    image='./interface/11.PNG', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_11 = visual.Slider(win=win, name='slider_11',
    size=(400,50), pos=(263.5, -151.5), units=None,
    labels=None, ticks=(0, 2000),
    granularity=1, style=['rating', 'whiteOnBlack'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_x2negd = visual.TextStim(win=win, name='text_x2negd',
    text=None,
    font='Arial',
    pos=(-155.3, 151.6), height=34, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_L_3 = visual.TextStim(win=win, name='text_L_3',
    text=None,
    font='Arial',
    pos=(-155.3, 0), height=34, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ratingText_11 = visual.TextStim(win=win, name='ratingText_11',
    text=slider_11.markerPos,
    font='Arial',
    pos=(272.9, 0), height=36, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
OKbutton_11 = visual.ImageStim(
    win=win,
    name='OKbutton_11', 
    image='./interface/OKbutton.png', mask=None,
    ori=0, pos=(0, -300), size=(150,76),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='experiment end \n              \nwait for instructor',
    font='Arial',
    pos=(0, 0), height=37, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def utility(x,alpha):
    return x**alpha
def utilityneg(x,alpha):
    return -x**alpha
end_to_rslt_key = keyboard.Keyboard()

# Initialize components for Routine "result"
resultClock = core.Clock()
image_rslt = visual.ImageStim(
    win=win,
    name='image_rslt', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(864, 576),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
end_exp_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionComponents = [text_ins, OKbutton, mouse]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_ins* updates
    if text_ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_ins.frameNStart = frameN  # exact frame index
        text_ins.tStart = t  # local t and not account for scr refresh
        text_ins.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_ins, 'tStartRefresh')  # time at next scr refresh
        text_ins.setAutoDraw(True)
    
    # *OKbutton* updates
    if OKbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OKbutton.frameNStart = frameN  # exact frame index
        OKbutton.tStart = t  # local t and not account for scr refresh
        OKbutton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton, 'tStartRefresh')  # time at next scr refresh
        OKbutton.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton]:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)

# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_1"-------
continueRoutine = True
# update component parameters for each repeat
slider_1.reset()
# setup some python lists for storing info about the mouse_1
mouse_1.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
trial_1Components = [interface_1, slider_1, ratingText_1, OKbutton_1, mouse_1]
for thisComponent in trial_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_1"-------
while continueRoutine:
    # get current time
    t = trial_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_1* updates
    if interface_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_1.frameNStart = frameN  # exact frame index
        interface_1.tStart = t  # local t and not account for scr refresh
        interface_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_1, 'tStartRefresh')  # time at next scr refresh
        interface_1.setAutoDraw(True)
    
    # *slider_1* updates
    if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_1.frameNStart = frameN  # exact frame index
        slider_1.tStart = t  # local t and not account for scr refresh
        slider_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
        slider_1.setAutoDraw(True)
    
    # *ratingText_1* updates
    if ratingText_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_1.frameNStart = frameN  # exact frame index
        ratingText_1.tStart = t  # local t and not account for scr refresh
        ratingText_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_1, 'tStartRefresh')  # time at next scr refresh
        ratingText_1.setAutoDraw(True)
    
    # *OKbutton_1* updates
    if OKbutton_1.status == NOT_STARTED and slider_1.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_1.frameNStart = frameN  # exact frame index
        OKbutton_1.tStart = t  # local t and not account for scr refresh
        OKbutton_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_1, 'tStartRefresh')  # time at next scr refresh
        OKbutton_1.setAutoDraw(True)
    # *mouse_1* updates
    if mouse_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_1.frameNStart = frameN  # exact frame index
        mouse_1.tStart = t  # local t and not account for scr refresh
        mouse_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_1, 'tStartRefresh')  # time at next scr refresh
        mouse_1.status = STARTED
        mouse_1.mouseClock.reset()
        prevButtonState = mouse_1.getPressed()  # if button is down already this ISN'T a new click
    if mouse_1.status == STARTED:  # only update if started and not finished!
        buttons = mouse_1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_1]:
                    if obj.contains(mouse_1):
                        gotValidClick = True
                        mouse_1.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_1.markerPos != None:
        ratingText_1.text = int(slider_1.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_1"-------
for thisComponent in trial_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_1.response', slider_1.getRating())
thisExp.addData('slider_1.rt', slider_1.getRT())
thisExp.addData('slider_1.history', slider_1.getHistory())
thisExp.addData('slider_1.started', slider_1.tStartRefresh)
thisExp.addData('slider_1.stopped', slider_1.tStopRefresh)
thisExp.addData('ratingText_1.started', ratingText_1.tStartRefresh)
thisExp.addData('ratingText_1.stopped', ratingText_1.tStopRefresh)
# store data for thisExp (ExperimentHandler)

L = slider_1.markerPos
# the Routine "trial_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_2"-------
continueRoutine = True
# update component parameters for each repeat
slider_2.reset()
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
trial_2Components = [interface_2, slider_2, ratingText_2, OKbutton_2, mouse_2]
for thisComponent in trial_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_2"-------
while continueRoutine:
    # get current time
    t = trial_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_2* updates
    if interface_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_2.frameNStart = frameN  # exact frame index
        interface_2.tStart = t  # local t and not account for scr refresh
        interface_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_2, 'tStartRefresh')  # time at next scr refresh
        interface_2.setAutoDraw(True)
    
    # *slider_2* updates
    if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_2.frameNStart = frameN  # exact frame index
        slider_2.tStart = t  # local t and not account for scr refresh
        slider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
        slider_2.setAutoDraw(True)
    
    # *ratingText_2* updates
    if ratingText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_2.frameNStart = frameN  # exact frame index
        ratingText_2.tStart = t  # local t and not account for scr refresh
        ratingText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_2, 'tStartRefresh')  # time at next scr refresh
        ratingText_2.setAutoDraw(True)
    
    # *OKbutton_2* updates
    if OKbutton_2.status == NOT_STARTED and slider_2.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_2.frameNStart = frameN  # exact frame index
        OKbutton_2.tStart = t  # local t and not account for scr refresh
        OKbutton_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_2, 'tStartRefresh')  # time at next scr refresh
        OKbutton_2.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_2]:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_2.markerPos != None:
        ratingText_2.text = int(slider_2.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_2"-------
for thisComponent in trial_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_2.response', slider_2.getRating())
thisExp.addData('slider_2.rt', slider_2.getRT())
thisExp.addData('slider_2.history', slider_2.getHistory())
thisExp.addData('slider_2.started', slider_2.tStartRefresh)
thisExp.addData('slider_2.stopped', slider_2.tStopRefresh)
thisExp.addData('ratingText_2.started', ratingText_2.tStartRefresh)
thisExp.addData('ratingText_2.stopped', ratingText_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x1pos = slider_2.markerPos

# the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_3"-------
continueRoutine = True
# update component parameters for each repeat
slider_3.reset()
# setup some python lists for storing info about the mouse_3
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
slider_3.ticks = (x1pos,2000)
text_x1pos.text = int(x1pos)
# keep track of which components have finished
trial_3Components = [interface_3, slider_3, text_x1pos, ratingText_3, OKbutton_3, mouse_3]
for thisComponent in trial_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_3"-------
while continueRoutine:
    # get current time
    t = trial_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_3* updates
    if interface_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_3.frameNStart = frameN  # exact frame index
        interface_3.tStart = t  # local t and not account for scr refresh
        interface_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_3, 'tStartRefresh')  # time at next scr refresh
        interface_3.setAutoDraw(True)
    
    # *slider_3* updates
    if slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_3.frameNStart = frameN  # exact frame index
        slider_3.tStart = t  # local t and not account for scr refresh
        slider_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
        slider_3.setAutoDraw(True)
    
    # *text_x1pos* updates
    if text_x1pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1pos.frameNStart = frameN  # exact frame index
        text_x1pos.tStart = t  # local t and not account for scr refresh
        text_x1pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1pos, 'tStartRefresh')  # time at next scr refresh
        text_x1pos.setAutoDraw(True)
    
    # *ratingText_3* updates
    if ratingText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_3.frameNStart = frameN  # exact frame index
        ratingText_3.tStart = t  # local t and not account for scr refresh
        ratingText_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_3, 'tStartRefresh')  # time at next scr refresh
        ratingText_3.setAutoDraw(True)
    
    # *OKbutton_3* updates
    if OKbutton_3.status == NOT_STARTED and slider_3.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_3.frameNStart = frameN  # exact frame index
        OKbutton_3.tStart = t  # local t and not account for scr refresh
        OKbutton_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_3, 'tStartRefresh')  # time at next scr refresh
        OKbutton_3.setAutoDraw(True)
    # *mouse_3* updates
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_3]:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_3.markerPos != None:
        ratingText_3.text = int(slider_3.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_3"-------
for thisComponent in trial_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_3.response', slider_3.getRating())
thisExp.addData('slider_3.rt', slider_3.getRT())
thisExp.addData('slider_3.history', slider_3.getHistory())
thisExp.addData('slider_3.started', slider_3.tStartRefresh)
thisExp.addData('slider_3.stopped', slider_3.tStopRefresh)
thisExp.addData('ratingText_3.started', ratingText_3.tStartRefresh)
thisExp.addData('ratingText_3.stopped', ratingText_3.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x2pos = slider_3.markerPos
# the Routine "trial_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_4"-------
continueRoutine = True
# update component parameters for each repeat
slider_4.reset()
# setup some python lists for storing info about the mouse_4
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
slider_4.ticks = (x2pos,2000)
text_x2pos.text = int(x2pos)
# keep track of which components have finished
trial_4Components = [interface_4, slider_4, text_x2pos, ratingText_4, OKbutton_4, mouse_4]
for thisComponent in trial_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_4"-------
while continueRoutine:
    # get current time
    t = trial_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_4* updates
    if interface_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_4.frameNStart = frameN  # exact frame index
        interface_4.tStart = t  # local t and not account for scr refresh
        interface_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_4, 'tStartRefresh')  # time at next scr refresh
        interface_4.setAutoDraw(True)
    
    # *slider_4* updates
    if slider_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_4.frameNStart = frameN  # exact frame index
        slider_4.tStart = t  # local t and not account for scr refresh
        slider_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_4, 'tStartRefresh')  # time at next scr refresh
        slider_4.setAutoDraw(True)
    
    # *text_x2pos* updates
    if text_x2pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x2pos.frameNStart = frameN  # exact frame index
        text_x2pos.tStart = t  # local t and not account for scr refresh
        text_x2pos.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x2pos, 'tStartRefresh')  # time at next scr refresh
        text_x2pos.setAutoDraw(True)
    
    # *ratingText_4* updates
    if ratingText_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_4.frameNStart = frameN  # exact frame index
        ratingText_4.tStart = t  # local t and not account for scr refresh
        ratingText_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_4, 'tStartRefresh')  # time at next scr refresh
        ratingText_4.setAutoDraw(True)
    
    # *OKbutton_4* updates
    if OKbutton_4.status == NOT_STARTED and slider_4.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_4.frameNStart = frameN  # exact frame index
        OKbutton_4.tStart = t  # local t and not account for scr refresh
        OKbutton_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_4, 'tStartRefresh')  # time at next scr refresh
        OKbutton_4.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_4]:
                    if obj.contains(mouse_4):
                        gotValidClick = True
                        mouse_4.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_4.markerPos != None:
        ratingText_4.text = int(slider_4.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_4"-------
for thisComponent in trial_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_4.response', slider_4.getRating())
thisExp.addData('slider_4.rt', slider_4.getRT())
thisExp.addData('slider_4.history', slider_4.getHistory())
thisExp.addData('slider_4.started', slider_4.tStartRefresh)
thisExp.addData('slider_4.stopped', slider_4.tStopRefresh)
thisExp.addData('ratingText_4.started', ratingText_4.tStartRefresh)
thisExp.addData('ratingText_4.stopped', ratingText_4.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x3pos = slider_4.markerPos
# the Routine "trial_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_5"-------
continueRoutine = True
# update component parameters for each repeat
slider_5.reset()
# setup some python lists for storing info about the mouse_5
mouse_5.clicked_name = []
gotValidClick = False  # until a click is received
slider_5.ticks = (0,x1pos)
text_x1pos_2.text = int(x1pos)
# keep track of which components have finished
trial_5Components = [interface_5, slider_5, text_x1pos_2, ratingText_5, OKbutton_5, mouse_5]
for thisComponent in trial_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_5"-------
while continueRoutine:
    # get current time
    t = trial_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_5* updates
    if interface_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_5.frameNStart = frameN  # exact frame index
        interface_5.tStart = t  # local t and not account for scr refresh
        interface_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_5, 'tStartRefresh')  # time at next scr refresh
        interface_5.setAutoDraw(True)
    
    # *slider_5* updates
    if slider_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_5.frameNStart = frameN  # exact frame index
        slider_5.tStart = t  # local t and not account for scr refresh
        slider_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_5, 'tStartRefresh')  # time at next scr refresh
        slider_5.setAutoDraw(True)
    
    # *text_x1pos_2* updates
    if text_x1pos_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1pos_2.frameNStart = frameN  # exact frame index
        text_x1pos_2.tStart = t  # local t and not account for scr refresh
        text_x1pos_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1pos_2, 'tStartRefresh')  # time at next scr refresh
        text_x1pos_2.setAutoDraw(True)
    
    # *ratingText_5* updates
    if ratingText_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_5.frameNStart = frameN  # exact frame index
        ratingText_5.tStart = t  # local t and not account for scr refresh
        ratingText_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_5, 'tStartRefresh')  # time at next scr refresh
        ratingText_5.setAutoDraw(True)
    
    # *OKbutton_5* updates
    if OKbutton_5.status == NOT_STARTED and slider_5.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_5.frameNStart = frameN  # exact frame index
        OKbutton_5.tStart = t  # local t and not account for scr refresh
        OKbutton_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_5, 'tStartRefresh')  # time at next scr refresh
        OKbutton_5.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_5]:
                    if obj.contains(mouse_5):
                        gotValidClick = True
                        mouse_5.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_5.markerPos != None:
        ratingText_5.text = int(slider_5.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_5"-------
for thisComponent in trial_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_5.response', slider_5.getRating())
thisExp.addData('slider_5.rt', slider_5.getRT())
thisExp.addData('slider_5.history', slider_5.getHistory())
thisExp.addData('slider_5.started', slider_5.tStartRefresh)
thisExp.addData('slider_5.stopped', slider_5.tStopRefresh)
thisExp.addData('ratingText_5.started', ratingText_5.tStartRefresh)
thisExp.addData('ratingText_5.stopped', ratingText_5.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x2posd = slider_5.markerPos
# the Routine "trial_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_6"-------
continueRoutine = True
# update component parameters for each repeat
slider_6.reset()
# setup some python lists for storing info about the mouse_6
mouse_6.clicked_name = []
gotValidClick = False  # until a click is received
slider_6.ticks = (0,x2posd)
text_x2posd.text = int(x2posd)
# keep track of which components have finished
trial_6Components = [interface_6, slider_6, text_x2posd, ratingText_6, OKbutton_6, mouse_6]
for thisComponent in trial_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_6"-------
while continueRoutine:
    # get current time
    t = trial_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_6* updates
    if interface_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_6.frameNStart = frameN  # exact frame index
        interface_6.tStart = t  # local t and not account for scr refresh
        interface_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_6, 'tStartRefresh')  # time at next scr refresh
        interface_6.setAutoDraw(True)
    
    # *slider_6* updates
    if slider_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_6.frameNStart = frameN  # exact frame index
        slider_6.tStart = t  # local t and not account for scr refresh
        slider_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_6, 'tStartRefresh')  # time at next scr refresh
        slider_6.setAutoDraw(True)
    
    # *text_x2posd* updates
    if text_x2posd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x2posd.frameNStart = frameN  # exact frame index
        text_x2posd.tStart = t  # local t and not account for scr refresh
        text_x2posd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x2posd, 'tStartRefresh')  # time at next scr refresh
        text_x2posd.setAutoDraw(True)
    
    # *ratingText_6* updates
    if ratingText_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_6.frameNStart = frameN  # exact frame index
        ratingText_6.tStart = t  # local t and not account for scr refresh
        ratingText_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_6, 'tStartRefresh')  # time at next scr refresh
        ratingText_6.setAutoDraw(True)
    
    # *OKbutton_6* updates
    if OKbutton_6.status == NOT_STARTED and slider_6.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_6.frameNStart = frameN  # exact frame index
        OKbutton_6.tStart = t  # local t and not account for scr refresh
        OKbutton_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_6, 'tStartRefresh')  # time at next scr refresh
        OKbutton_6.setAutoDraw(True)
    # *mouse_6* updates
    if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_6.frameNStart = frameN  # exact frame index
        mouse_6.tStart = t  # local t and not account for scr refresh
        mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
        mouse_6.status = STARTED
        mouse_6.mouseClock.reset()
        prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
    if mouse_6.status == STARTED:  # only update if started and not finished!
        buttons = mouse_6.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_6]:
                    if obj.contains(mouse_6):
                        gotValidClick = True
                        mouse_6.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_6.markerPos != None:
        ratingText_6.text = int(slider_6.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_6"-------
for thisComponent in trial_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_6.response', slider_6.getRating())
thisExp.addData('slider_6.rt', slider_6.getRT())
thisExp.addData('slider_6.history', slider_6.getHistory())
thisExp.addData('slider_6.started', slider_6.tStartRefresh)
thisExp.addData('slider_6.stopped', slider_6.tStopRefresh)
thisExp.addData('ratingText_6.started', ratingText_6.tStartRefresh)
thisExp.addData('ratingText_6.stopped', ratingText_6.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x3posd = slider_6.markerPos
# the Routine "trial_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_7"-------
continueRoutine = True
# update component parameters for each repeat
slider_7.reset()
# setup some python lists for storing info about the mouse_7
mouse_7.clicked_name = []
gotValidClick = False  # until a click is received
slider_7.ticks = (L,0)
text_L.text = int(L)
# keep track of which components have finished
trial_7Components = [interface_7, slider_7, text_L, ratingText_7, OKbutton_7, mouse_7]
for thisComponent in trial_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_7"-------
while continueRoutine:
    # get current time
    t = trial_7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_7* updates
    if interface_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_7.frameNStart = frameN  # exact frame index
        interface_7.tStart = t  # local t and not account for scr refresh
        interface_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_7, 'tStartRefresh')  # time at next scr refresh
        interface_7.setAutoDraw(True)
    
    # *slider_7* updates
    if slider_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_7.frameNStart = frameN  # exact frame index
        slider_7.tStart = t  # local t and not account for scr refresh
        slider_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_7, 'tStartRefresh')  # time at next scr refresh
        slider_7.setAutoDraw(True)
    
    # *text_L* updates
    if text_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L.frameNStart = frameN  # exact frame index
        text_L.tStart = t  # local t and not account for scr refresh
        text_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L, 'tStartRefresh')  # time at next scr refresh
        text_L.setAutoDraw(True)
    
    # *ratingText_7* updates
    if ratingText_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_7.frameNStart = frameN  # exact frame index
        ratingText_7.tStart = t  # local t and not account for scr refresh
        ratingText_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_7, 'tStartRefresh')  # time at next scr refresh
        ratingText_7.setAutoDraw(True)
    
    # *OKbutton_7* updates
    if OKbutton_7.status == NOT_STARTED and slider_7.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_7.frameNStart = frameN  # exact frame index
        OKbutton_7.tStart = t  # local t and not account for scr refresh
        OKbutton_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_7, 'tStartRefresh')  # time at next scr refresh
        OKbutton_7.setAutoDraw(True)
    # *mouse_7* updates
    if mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_7.frameNStart = frameN  # exact frame index
        mouse_7.tStart = t  # local t and not account for scr refresh
        mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
        mouse_7.status = STARTED
        mouse_7.mouseClock.reset()
        prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
    if mouse_7.status == STARTED:  # only update if started and not finished!
        buttons = mouse_7.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_7]:
                    if obj.contains(mouse_7):
                        gotValidClick = True
                        mouse_7.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_7.markerPos != None:
        ratingText_7.text = int(slider_7.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_7"-------
for thisComponent in trial_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_7.response', slider_7.getRating())
thisExp.addData('slider_7.rt', slider_7.getRT())
thisExp.addData('slider_7.history', slider_7.getHistory())
thisExp.addData('slider_7.started', slider_7.tStartRefresh)
thisExp.addData('slider_7.stopped', slider_7.tStopRefresh)
thisExp.addData('ratingText_7.started', ratingText_7.tStartRefresh)
thisExp.addData('ratingText_7.stopped', ratingText_7.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x1neg = slider_7.markerPos
# the Routine "trial_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_8"-------
continueRoutine = True
# update component parameters for each repeat
slider_8.reset()
# setup some python lists for storing info about the mouse_8
mouse_8.clicked_name = []
gotValidClick = False  # until a click is received
slider_8.ticks = (x1neg,0)
text_x1neg.text = int(x1neg)
# keep track of which components have finished
trial_8Components = [interface_8, slider_8, text_x1neg, ratingText_8, OKbutton_8, mouse_8]
for thisComponent in trial_8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_8"-------
while continueRoutine:
    # get current time
    t = trial_8Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_8Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_8* updates
    if interface_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_8.frameNStart = frameN  # exact frame index
        interface_8.tStart = t  # local t and not account for scr refresh
        interface_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_8, 'tStartRefresh')  # time at next scr refresh
        interface_8.setAutoDraw(True)
    
    # *slider_8* updates
    if slider_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_8.frameNStart = frameN  # exact frame index
        slider_8.tStart = t  # local t and not account for scr refresh
        slider_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_8, 'tStartRefresh')  # time at next scr refresh
        slider_8.setAutoDraw(True)
    
    # *text_x1neg* updates
    if text_x1neg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1neg.frameNStart = frameN  # exact frame index
        text_x1neg.tStart = t  # local t and not account for scr refresh
        text_x1neg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1neg, 'tStartRefresh')  # time at next scr refresh
        text_x1neg.setAutoDraw(True)
    
    # *ratingText_8* updates
    if ratingText_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_8.frameNStart = frameN  # exact frame index
        ratingText_8.tStart = t  # local t and not account for scr refresh
        ratingText_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_8, 'tStartRefresh')  # time at next scr refresh
        ratingText_8.setAutoDraw(True)
    
    # *OKbutton_8* updates
    if OKbutton_8.status == NOT_STARTED and slider_8.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_8.frameNStart = frameN  # exact frame index
        OKbutton_8.tStart = t  # local t and not account for scr refresh
        OKbutton_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_8, 'tStartRefresh')  # time at next scr refresh
        OKbutton_8.setAutoDraw(True)
    # *mouse_8* updates
    if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_8.frameNStart = frameN  # exact frame index
        mouse_8.tStart = t  # local t and not account for scr refresh
        mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
        mouse_8.status = STARTED
        mouse_8.mouseClock.reset()
        prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
    if mouse_8.status == STARTED:  # only update if started and not finished!
        buttons = mouse_8.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_8]:
                    if obj.contains(mouse_8):
                        gotValidClick = True
                        mouse_8.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_8.markerPos != None:
        ratingText_8.text = int(slider_8.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_8"-------
for thisComponent in trial_8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_8.response', slider_8.getRating())
thisExp.addData('slider_8.rt', slider_8.getRT())
thisExp.addData('slider_8.history', slider_8.getHistory())
thisExp.addData('slider_8.started', slider_8.tStartRefresh)
thisExp.addData('slider_8.stopped', slider_8.tStopRefresh)
thisExp.addData('ratingText_8.started', ratingText_8.tStartRefresh)
thisExp.addData('ratingText_8.stopped', ratingText_8.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x2neg = slider_8.markerPos
# the Routine "trial_8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_9"-------
continueRoutine = True
# update component parameters for each repeat
slider_9.reset()
# setup some python lists for storing info about the mouse_9
mouse_9.clicked_name = []
gotValidClick = False  # until a click is received
slider_9.ticks = (x2neg,0)
text_x2neg.text = int(x2neg)
# keep track of which components have finished
trial_9Components = [interface_9, slider_9, text_x2neg, ratingText_9, OKbutton_9, mouse_9]
for thisComponent in trial_9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_9"-------
while continueRoutine:
    # get current time
    t = trial_9Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_9Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_9* updates
    if interface_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_9.frameNStart = frameN  # exact frame index
        interface_9.tStart = t  # local t and not account for scr refresh
        interface_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_9, 'tStartRefresh')  # time at next scr refresh
        interface_9.setAutoDraw(True)
    
    # *slider_9* updates
    if slider_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_9.frameNStart = frameN  # exact frame index
        slider_9.tStart = t  # local t and not account for scr refresh
        slider_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_9, 'tStartRefresh')  # time at next scr refresh
        slider_9.setAutoDraw(True)
    
    # *text_x2neg* updates
    if text_x2neg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x2neg.frameNStart = frameN  # exact frame index
        text_x2neg.tStart = t  # local t and not account for scr refresh
        text_x2neg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x2neg, 'tStartRefresh')  # time at next scr refresh
        text_x2neg.setAutoDraw(True)
    
    # *ratingText_9* updates
    if ratingText_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_9.frameNStart = frameN  # exact frame index
        ratingText_9.tStart = t  # local t and not account for scr refresh
        ratingText_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_9, 'tStartRefresh')  # time at next scr refresh
        ratingText_9.setAutoDraw(True)
    
    # *OKbutton_9* updates
    if OKbutton_9.status == NOT_STARTED and slider_9.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_9.frameNStart = frameN  # exact frame index
        OKbutton_9.tStart = t  # local t and not account for scr refresh
        OKbutton_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_9, 'tStartRefresh')  # time at next scr refresh
        OKbutton_9.setAutoDraw(True)
    # *mouse_9* updates
    if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_9.frameNStart = frameN  # exact frame index
        mouse_9.tStart = t  # local t and not account for scr refresh
        mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
        mouse_9.status = STARTED
        mouse_9.mouseClock.reset()
        prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
    if mouse_9.status == STARTED:  # only update if started and not finished!
        buttons = mouse_9.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_9]:
                    if obj.contains(mouse_9):
                        gotValidClick = True
                        mouse_9.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_9.markerPos != None:
        ratingText_9.text = int(slider_9.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_9"-------
for thisComponent in trial_9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_9.response', slider_9.getRating())
thisExp.addData('slider_9.rt', slider_9.getRT())
thisExp.addData('slider_9.history', slider_9.getHistory())
thisExp.addData('slider_9.started', slider_9.tStartRefresh)
thisExp.addData('slider_9.stopped', slider_9.tStopRefresh)
thisExp.addData('ratingText_9.started', ratingText_9.tStartRefresh)
thisExp.addData('ratingText_9.stopped', ratingText_9.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x3neg = slider_9.markerPos
# the Routine "trial_9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_10"-------
continueRoutine = True
# update component parameters for each repeat
slider_10.reset()
# setup some python lists for storing info about the mouse_10
mouse_10.clicked_name = []
gotValidClick = False  # until a click is received
slider_10.ticks = (L,x1neg)
text_x1neg_2.text = int(x1neg)
text_L_2.text = int(L)
# keep track of which components have finished
trial_10Components = [interface_10, slider_10, text_x1neg_2, text_L_2, ratingText_10, OKbutton_10, mouse_10]
for thisComponent in trial_10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_10"-------
while continueRoutine:
    # get current time
    t = trial_10Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_10Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_10* updates
    if interface_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_10.frameNStart = frameN  # exact frame index
        interface_10.tStart = t  # local t and not account for scr refresh
        interface_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_10, 'tStartRefresh')  # time at next scr refresh
        interface_10.setAutoDraw(True)
    
    # *slider_10* updates
    if slider_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_10.frameNStart = frameN  # exact frame index
        slider_10.tStart = t  # local t and not account for scr refresh
        slider_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_10, 'tStartRefresh')  # time at next scr refresh
        slider_10.setAutoDraw(True)
    
    # *text_x1neg_2* updates
    if text_x1neg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x1neg_2.frameNStart = frameN  # exact frame index
        text_x1neg_2.tStart = t  # local t and not account for scr refresh
        text_x1neg_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x1neg_2, 'tStartRefresh')  # time at next scr refresh
        text_x1neg_2.setAutoDraw(True)
    
    # *text_L_2* updates
    if text_L_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L_2.frameNStart = frameN  # exact frame index
        text_L_2.tStart = t  # local t and not account for scr refresh
        text_L_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L_2, 'tStartRefresh')  # time at next scr refresh
        text_L_2.setAutoDraw(True)
    
    # *ratingText_10* updates
    if ratingText_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_10.frameNStart = frameN  # exact frame index
        ratingText_10.tStart = t  # local t and not account for scr refresh
        ratingText_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_10, 'tStartRefresh')  # time at next scr refresh
        ratingText_10.setAutoDraw(True)
    
    # *OKbutton_10* updates
    if OKbutton_10.status == NOT_STARTED and slider_10.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_10.frameNStart = frameN  # exact frame index
        OKbutton_10.tStart = t  # local t and not account for scr refresh
        OKbutton_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_10, 'tStartRefresh')  # time at next scr refresh
        OKbutton_10.setAutoDraw(True)
    # *mouse_10* updates
    if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_10.frameNStart = frameN  # exact frame index
        mouse_10.tStart = t  # local t and not account for scr refresh
        mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
        mouse_10.status = STARTED
        mouse_10.mouseClock.reset()
        prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
    if mouse_10.status == STARTED:  # only update if started and not finished!
        buttons = mouse_10.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_10]:
                    if obj.contains(mouse_10):
                        gotValidClick = True
                        mouse_10.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_10.markerPos != None:
        ratingText_10.text = int(slider_10.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_10"-------
for thisComponent in trial_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_10.response', slider_10.getRating())
thisExp.addData('slider_10.rt', slider_10.getRT())
thisExp.addData('slider_10.history', slider_10.getHistory())
thisExp.addData('slider_10.started', slider_10.tStartRefresh)
thisExp.addData('slider_10.stopped', slider_10.tStopRefresh)
thisExp.addData('ratingText_10.started', ratingText_10.tStartRefresh)
thisExp.addData('ratingText_10.stopped', ratingText_10.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x2negd = slider_10.markerPos
# the Routine "trial_10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_11"-------
continueRoutine = True
# update component parameters for each repeat
slider_11.reset()
# setup some python lists for storing info about the mouse_11
mouse_11.clicked_name = []
gotValidClick = False  # until a click is received
slider_11.ticks = (L,x2negd)
text_L_3.text = int(L)
text_x2negd.text = int(x2negd)
# keep track of which components have finished
trial_11Components = [interface_11, slider_11, text_x2negd, text_L_3, ratingText_11, OKbutton_11, mouse_11]
for thisComponent in trial_11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_11Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_11"-------
while continueRoutine:
    # get current time
    t = trial_11Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_11Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interface_11* updates
    if interface_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interface_11.frameNStart = frameN  # exact frame index
        interface_11.tStart = t  # local t and not account for scr refresh
        interface_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interface_11, 'tStartRefresh')  # time at next scr refresh
        interface_11.setAutoDraw(True)
    
    # *slider_11* updates
    if slider_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_11.frameNStart = frameN  # exact frame index
        slider_11.tStart = t  # local t and not account for scr refresh
        slider_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_11, 'tStartRefresh')  # time at next scr refresh
        slider_11.setAutoDraw(True)
    
    # *text_x2negd* updates
    if text_x2negd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_x2negd.frameNStart = frameN  # exact frame index
        text_x2negd.tStart = t  # local t and not account for scr refresh
        text_x2negd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_x2negd, 'tStartRefresh')  # time at next scr refresh
        text_x2negd.setAutoDraw(True)
    
    # *text_L_3* updates
    if text_L_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_L_3.frameNStart = frameN  # exact frame index
        text_L_3.tStart = t  # local t and not account for scr refresh
        text_L_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_L_3, 'tStartRefresh')  # time at next scr refresh
        text_L_3.setAutoDraw(True)
    
    # *ratingText_11* updates
    if ratingText_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ratingText_11.frameNStart = frameN  # exact frame index
        ratingText_11.tStart = t  # local t and not account for scr refresh
        ratingText_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ratingText_11, 'tStartRefresh')  # time at next scr refresh
        ratingText_11.setAutoDraw(True)
    
    # *OKbutton_11* updates
    if OKbutton_11.status == NOT_STARTED and slider_11.markerPos != None:
        # keep track of start time/frame for later
        OKbutton_11.frameNStart = frameN  # exact frame index
        OKbutton_11.tStart = t  # local t and not account for scr refresh
        OKbutton_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OKbutton_11, 'tStartRefresh')  # time at next scr refresh
        OKbutton_11.setAutoDraw(True)
    # *mouse_11* updates
    if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_11.frameNStart = frameN  # exact frame index
        mouse_11.tStart = t  # local t and not account for scr refresh
        mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
        mouse_11.status = STARTED
        mouse_11.mouseClock.reset()
        prevButtonState = mouse_11.getPressed()  # if button is down already this ISN'T a new click
    if mouse_11.status == STARTED:  # only update if started and not finished!
        buttons = mouse_11.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [OKbutton_11]:
                    if obj.contains(mouse_11):
                        gotValidClick = True
                        mouse_11.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if slider_11.markerPos != None:
        ratingText_11.text = int(slider_11.markerPos)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_11"-------
for thisComponent in trial_11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_11.response', slider_11.getRating())
thisExp.addData('slider_11.rt', slider_11.getRT())
thisExp.addData('slider_11.history', slider_11.getHistory())
thisExp.addData('slider_11.started', slider_11.tStartRefresh)
thisExp.addData('slider_11.stopped', slider_11.tStopRefresh)
thisExp.addData('ratingText_11.started', ratingText_11.tStartRefresh)
thisExp.addData('ratingText_11.stopped', ratingText_11.tStopRefresh)
# store data for thisExp (ExperimentHandler)

x3negd = slider_11.markerPos

# the Routine "trial_11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
end_to_rslt_key.keys = []
end_to_rslt_key.rt = []
_end_to_rslt_key_allKeys = []
# keep track of which components have finished
endComponents = [text_end, end_to_rslt_key]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    
    # *end_to_rslt_key* updates
    waitOnFlip = False
    if end_to_rslt_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_to_rslt_key.frameNStart = frameN  # exact frame index
        end_to_rslt_key.tStart = t  # local t and not account for scr refresh
        end_to_rslt_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_to_rslt_key, 'tStartRefresh')  # time at next scr refresh
        end_to_rslt_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_to_rslt_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_to_rslt_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_to_rslt_key.status == STARTED and not waitOnFlip:
        theseKeys = end_to_rslt_key.getKeys(keyList=['right'], waitRelease=False)
        _end_to_rslt_key_allKeys.extend(theseKeys)
        if len(_end_to_rslt_key_allKeys):
            end_to_rslt_key.keys = _end_to_rslt_key_allKeys[-1].name  # just the last key pressed
            end_to_rslt_key.rt = _end_to_rslt_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
y = [-100, 50, 75, 87.5, 25, 12.5, -50, -25, -12.5, -75, -87.5, 0, 100]
x = [L, x1pos, x2pos, x3pos, x2posd, x3posd, x1neg, x2neg, x3neg, x2negd, x3negd, 0, 2000]
ypos = np.array([50, 75, 87.5, 25, 12.5, 0, 100])
yneg = np.array([-50, -25, -12.5, -75, -87.5, 0, -100])
xpos = np.array([x1pos, x2pos, x3pos, x2posd, x3posd, 0, 2000])
xneg = np.array([x1neg, x2neg, x3neg, x2negd, x3negd, 0, L])
ypos = np.sort(ypos)
xpos = np.sort(xpos)
xneg = np.sort(xneg)
yneg = np.sort(yneg)
negyneg = -yneg
negyneg = np.flip(np.sort(negyneg)) # values are positive now
negxneg = -xneg
negxneg = np.flip(np.sort(negxneg)) # values are positive now



alphapos = curve_fit(utility,xpos,ypos)
alphaneg = curve_fit(utility,negxneg,negyneg)

plt.plot(x, y, 'g.')
plt.plot(xpos, utility(xpos, alphapos[0]), 'r-',label = alphapos[0])
plt.plot(xneg, utilityneg(negxneg, alphaneg[0]), 'b-',label = alphaneg[0])
plt.legend()
plt.savefig(filename+'.png')
image_rslt.image = filename+'.png'

thisExp.addData('alphapos', alphapos)
thisExp.addData('alphaneg', alphaneg)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "result"-------
continueRoutine = True
# update component parameters for each repeat
end_exp_key.keys = []
end_exp_key.rt = []
_end_exp_key_allKeys = []
# keep track of which components have finished
resultComponents = [image_rslt, end_exp_key]
for thisComponent in resultComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
resultClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "result"-------
while continueRoutine:
    # get current time
    t = resultClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=resultClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_rslt* updates
    if image_rslt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_rslt.frameNStart = frameN  # exact frame index
        image_rslt.tStart = t  # local t and not account for scr refresh
        image_rslt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_rslt, 'tStartRefresh')  # time at next scr refresh
        image_rslt.setAutoDraw(True)
    
    # *end_exp_key* updates
    waitOnFlip = False
    if end_exp_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_exp_key.frameNStart = frameN  # exact frame index
        end_exp_key.tStart = t  # local t and not account for scr refresh
        end_exp_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_exp_key, 'tStartRefresh')  # time at next scr refresh
        end_exp_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_exp_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_exp_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_exp_key.status == STARTED and not waitOnFlip:
        theseKeys = end_exp_key.getKeys(keyList=['space'], waitRelease=False)
        _end_exp_key_allKeys.extend(theseKeys)
        if len(_end_exp_key_allKeys):
            end_exp_key.keys = _end_exp_key_allKeys[-1].name  # just the last key pressed
            end_exp_key.rt = _end_exp_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resultComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "result"-------
for thisComponent in resultComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "result" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
