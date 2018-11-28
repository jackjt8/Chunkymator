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
from pandas import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ospath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#script = os.path.realpath(__file__)

def saveFiles(cvfs, outputDir):
    for i in range(len(cvfs)):
        c = cvfs[i]
        
        charlen = len(str(len(cvfs))) + 1
        #print(str(i).zfill(charlen))
        name = os.path.join(outputDir, "interpolated-" + '1' + str(i).zfill(charlen) + ".json")
        c.setName("interpolated-" + str(i).zfill(charlen))
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

framerate = 60.0
frametime = 1.0/framerate

# Create list of key scenes
keyscenes = []

# Append scenes to list
temp_time = 0.0
step = 1.0
nameoffset = 10000

# Gets scenenames assuming default naming scheme is used
#   ie n10001, n10002, etc.
for i in range(0,65):
    scenename = 'n' + str(nameoffset + i) + '.json'
    #                   filenmae       time
    keyscenes.append([scenename, temp_time])
    temp_time += step
    
# Alt method is to just spam 
#   keyscenes.append([scenename, temp_time])
# with custom times

interp_mode = 'cubic'

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
    print("This script requires at least 4 input jsons to generate a route between them.")
    #return
while i < num:
    try:
        filename = keyscenes[i][0]
        print("loading ", filename)

        scene = cvf(filename)
        cvfList.append(scene)
#        print ("X: " + str(scene.getX()) +
#               " Y: " + str(scene.getY()) +
#               " Z: " + str(scene.getZ()) +
#               " Pitch: " + str(scene.getPitch()) +
#               " Yaw: " + str(scene.getYaw()))

        i += 1
    except EnvironmentError:
        print("could not get file #" + str(i + 1) + " please try again!")
        #return
print("done loading " + str(num) + " files.")

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
    
    camFoV.append(cvf_.getFoV())
    camDoF.append(cvf_.getDoF())
    camfocalOffset.append(cvf_.getfocalOffset())
     
    SunAltitude.append(cvf_.getSunAltitude())
    SunAzimuth.append(cvf_.getSunAzimuth())
    SunIntensity.append(cvf_.getSunIntensity())
    SunColR.append(cvf_.getSunColR())
    SunColG.append(cvf_.getSunColG())
    SunColB.append(cvf_.getSunColB())
    SkyLight.append(cvf_.getSkyLight())

print('cvf_.get done')

def interpT(t, tframe, x, kindtype):
    f = interpolate.interp1d(t, x, kind=kindtype)
    return f(tframe)

new_camX = interpT(keyscene_time, tframe, camX, interp_mode)
new_camY = interpT(keyscene_time, tframe, camY, interp_mode)
new_camZ = interpT(keyscene_time, tframe, camZ, interp_mode)
new_camPitch = interpT(keyscene_time, tframe, camPitch, interp_mode)
new_camYaw = interpT(keyscene_time, tframe, camYaw, interp_mode)

new_camFoV = interpT(keyscene_time, tframe, camFoV, interp_mode)

new_camDoF = interpT(keyscene_time, tframe, camDoF, interp_mode)
new_camDoF[new_camDoF < 0] = np.nan
new_camDoF = Series(new_camDoF).interpolate().values # linear interp where we get negative values

new_camfocalOffset = interpT(keyscene_time, tframe, camfocalOffset, interp_mode)
new_camfocalOffset[new_camfocalOffset < 0] = np.nan
new_camfocalOffset = Series(new_camfocalOffset).interpolate().values # linear interp where we get negative values

new_SunAltitude = interpT(keyscene_time, tframe, SunAltitude, interp_mode)
new_SunAzimuth = interpT(keyscene_time, tframe, SunAzimuth, interp_mode)
new_SunIntensity = interpT(keyscene_time, tframe, SunIntensity, interp_mode)
new_SunColR = interpT(keyscene_time, tframe, SunColR, interp_mode)
new_SunColG = interpT(keyscene_time, tframe, SunColG, interp_mode)
new_SunColB = interpT(keyscene_time, tframe, SunColB, interp_mode)
new_SkyLight = interpT(keyscene_time, tframe, SkyLight, interp_mode)


# Override settings.
#new_SkyLight = [round(x + 2) for x in new_SkyLight]

new_spp = [int(16) for x in new_SkyLight]
new_RD = [int(3) for x in new_SkyLight]
new_Width = [int(1920) for x in new_SkyLight]
new_Height = [int(1080) for x in new_SkyLight]

print('value interplotion done')

dp = 8
new_camX = np.round(new_camX, dp)
new_camY = np.round(new_camY, dp)
new_camZ = np.round(new_camZ, dp)
new_camPitch = np.round(new_camPitch, dp)
new_camYaw = np.round(new_camYaw, dp)

new_camFoV = np.round(new_camFoV, dp)
new_camDoF = np.round(new_camDoF, dp)
new_camfocalOffset = np.round(new_camfocalOffset, dp)

new_SunAltitude = np.round(new_SunAltitude, dp)
new_SunAzimuth = np.round(new_SunAzimuth, dp)
new_SunIntensity = np.round(new_SunIntensity, dp)
new_SunColR = np.round(new_SunColR, dp)
new_SunColG = np.round(new_SunColG, dp)
new_SunColB = np.round(new_SunColB, dp)
new_SkyLight = np.round(new_SkyLight, dp)

print('Rounding floats to 8DP')

new_cvfList = []
for i in range(len(new_camX)):
    new_cvfList.append(cvf(keyscenes[0][0])) # ie append a fresh cvf object

for i in range(len(new_camX)):
    new_cvfList[i].setspp(new_spp[i])
    new_cvfList[i].setRD(new_RD[i])
    new_cvfList[i].setWidth(new_Width[i])
    new_cvfList[i].setHeight(new_Height[i])
    
    new_cvfList[i].setX(new_camX[i])
    new_cvfList[i].setY(new_camY[i])
    new_cvfList[i].setZ(new_camZ[i])
    new_cvfList[i].setPitch(new_camPitch[i])
    new_cvfList[i].setYaw(new_camYaw[i])
    
    new_cvfList[i].setFoV(new_camFoV[i])
    new_cvfList[i].setDoF(new_camDoF[i])
    new_cvfList[i].setfocalOffset(new_camfocalOffset[i])
   
    new_cvfList[i].setSunAltitude(new_SunAltitude[i])
    new_cvfList[i].setSunAzimuth(new_SunAzimuth[i])
    new_cvfList[i].setSunIntensity(new_SunIntensity[i])
    new_cvfList[i].setSunColR(new_SunColR[i])
    new_cvfList[i].setSunColG(new_SunColG[i])
    new_cvfList[i].setSunColB(new_SunColB[i])
    new_cvfList[i].setSkyLight(new_SkyLight[i])
    
    new_cvfList[i].setsaveSnapshots()

print('new cvf list made & values set')


outputDir = 'output'
saveFiles(new_cvfList, outputDir)
print('write to file completed')

#plt.plot(new_camPitch)
#plt.plot(new_camYaw)

#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
## n is for reduced sample plotting
#n = int(framerate)/2
#
#ax.plot(-new_camX, new_camZ, new_camY)
#ax.plot(-new_camX[::n], new_camZ[::n], new_camY[::n])
##
#r = 20
#DcamX = r * np.sin(new_camPitch) * np.cos(new_camYaw)
#DcamZ = r * np.sin(new_camPitch) * np.sin(new_camYaw)
#DcamY = r * np.cos(new_camPitch)
#
#ax.plot(DcamX, DcamZ, DcamY, color='r') # Spherical plot of cam orientation


#ax.plot(DcamX[::n], DcamZ[::n], DcamY[::n]) # ie reduced sample plotting


#for i in range(0, len(new_camX), n):
#    tempx = [-new_camX[i], -new_camX[i] - DcamX[i]]
#    tempz = [new_camZ[i], new_camZ[i] - DcamZ[i]]
#    tempy = [new_camY[i], new_camY[i] - DcamY[i]]
#    ax.plot(tempx, tempz, tempy)
    
#a = Arrow3D([0,1],[0,1],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
#ax.add_artist(a)
    
#
#ax.set_xlabel('X axis')
#ax.set_ylabel('Z axis')
#ax.set_zlabel('Y axis')
#
#plt.show()

