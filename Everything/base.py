# -*- coding: utf-8 -*-
"""
Created on Sun Jul 01 21:10:01 2018

@author: jackjt8

title: Chunky JSON generator

ver: 0.0.1
"""
import json
from cvf import *
#from inspect import getsourcefile
#from os.path import abspath
import inspect, os
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ospath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#script = os.path.realpath(__file__)

def saveFiles(cvfs, outputDir):
    for i in range(len(cvfs)):
        c = cvfs[i]
        name = os.path.join(outputDir, "interpolated-" + str(i) + ".json")
        c.setName("interpolated-" + str(i))
#        print (str(i) + ": " +
#               ("X: %(x).2f " +
#                "Y: %(y).2f " +
#                "Z: %(z).2f " +
#                "Pitch: %(pitch).2f " +
#                "Yaw: %(yaw).2f " +
#                "SunAltitude: %(alt).2f " +
#                "SunAzimuth: %(azim).2f ") %
#               {
#            'x': c.getX(),
#            'y': c.getY(),
#            'z': c.getZ(),
#            'pitch': c.getPitch(),
#            'yaw': c.getYaw(),
#            'alt': c.getSunAltitude(),
#            'azim': c.getSunAzimuth()
#        })

        c.saveToFile(name)

#%%
#Test code

framerate = 15.0
frametime = 1.0/framerate

# Create list of key scenes
keyscenes = []

# Append scenes to list
#                   filenmae        time
keyscenes.append(['Landscape1.json', 0.0])
keyscenes.append(['Landscape1.json', 5.0])
#keyscenes.append(['Landscape1.json', 8.0])
#keyscenes.append(['Landscape1.json', 9.0])
#keyscenes.append(['Landscape1.json', 10.0])


# Extract keyscene time
keyscene_time = []
for x in keyscenes:
    keyscene_time.append(x[1])
nframe = (keyscene_time[-1] - keyscene_time[0]) / frametime #number of frames between first and last node
tframe = np.linspace(keyscene_time[0], keyscene_time[-1], int(nframe)) #time of each frame


num = len(keyscenes)

cvfList = []
i = 0
if num < 4:
    print "This script requires at least 4 input jsons to generate a route between them."
    #return
while i < num:
    try:
        filename = keyscenes[i][0]
        print "loading ", filename

        scene = cvf(filename)
        cvfList.append(scene)
        print ("X: " + str(scene.getX()) +
               " Y: " + str(scene.getY()) +
               " Z: " + str(scene.getZ()) +
               " Pitch: " + str(scene.getPitch()) +
               " Yaw: " + str(scene.getYaw()))

        i += 1
    except EnvironmentError:
        print "could not get file #" + str(i + 1) + " please try again!"
        #return
print "done loading " + str(num) + " files."

EXP = []
Wopac = []
Wvis = []
FogR = []
FogG = []
FogB = []
FogDen = []
camX = []
camY = []
camZ = []
camRoll = []
camPitch = []
camYaw = []
camFoV = []
camDoF = []
camfocalOffset = []
SunAltitude = []
SunAzimuth = []
SunIntensity = []
SunColR = []
SunColG = []
SunColB = []
SkyYaw = []
SkyLight = []
cloudSize = []
cloudX = []
cloudY = []
cloudZ = []

for cvf_ in cvfList:
    camX.append(cvf_.getX())
    camY.append(cvf_.getY())
    camZ.append(cvf_.getZ())
    camPitch.append(cvf_.getPitch())
    camYaw.append(cvf_.getYaw())


def interpT(t, tframe, x, kindtype):
    f = interpolate.interp1d(t, x, kind=kindtype)
    return f(tframe)


new_camX = interpT(keyscene_time, tframe, camX, 'quadratic')
new_camY = interpT(keyscene_time, tframe, camY, 'quadratic')
new_camZ = interpT(keyscene_time, tframe, camZ, 'quadratic')
new_camPitch = interpT(keyscene_time, tframe, camPitch, 'quadratic')%360
new_camYaw = interpT(keyscene_time, tframe, camYaw, 'quadratic')%360


new_cvfList = [cvfList[0]] * (len(new_camX)) # ie use keyscene 1 as base

for i in range(len(new_camX)):
    new_cvfList[i].setX(new_camX[i])
    new_cvfList[i].setY(new_camY[i])
    new_cvfList[i].setZ(new_camZ[i])
    new_cvfList[i].setPitch(new_camPitch[i])
    new_cvfList[i].setYaw(new_camYaw[i])


outputDir = 'output'
saveFiles(new_cvfList, outputDir)
# generate n new jsons based on json 0
# set new values to correct json
# write to file.




