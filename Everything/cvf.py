import json


def rad2deg(theta):
    if theta > 2 * 3.14159265358:
        return rad2deg(theta - 2 * 3.14159265358)
    if theta < 0.0:
        return rad2deg(theta + 2 * 3.14159265358)
    return theta * 180 / 3.14159265358


def deg2rad(theta):
    if theta > 360.0:
        return deg2rad(theta - 360)
    if theta < 0.0:
        return deg2rad(theta + 360)
    return theta * 3.14159265358 / 180


class cvf(object):
    
    # get MISC
    def getEXP(self):
        return self.inputJson['exposure']
    
    def getWopac(self):
        return self.inputJson['waterOpacity']
    
    def getWvis(self):
        return self.inputJson['waterVisibility']
    
    #%% Water Colour missing.
    
    #%%
    def getFogR(self):
        return self.inputJson['fogColor']['red'] 

    def getFogG(self):
        return self.inputJson['fogColor']['green']

    def getFogB(self):
        return self.inputJson['fogColor']['blue']
    
    def getFogDen(self):
        return self.inputJson['fogDensity']
    
    #%%
    # get camera
    #   position
    def getX(self):
        return self.inputJson['camera']['position']['x']

    def getY(self):
        return self.inputJson['camera']['position']['y']

    def getZ(self):
        return self.inputJson['camera']['position']['z']

    #   orientation

    def getRoll(self):
        return self.inputJson['camera']['orientation']['roll']
    
    def getPitch(self):
        return self.inputJson['camera']['orientation']['pitch']

    def getYaw(self):
        return self.inputJson['camera']['orientation']['yaw']

    #   other
    def getFoV(self):
        return self.inputJson['camera']['fov']
    
    def getDoF(self):
        return self.inputJson['camera']['dof']

    def getfocalOffset(self):
        return self.inputJson['camera']['focalOffset']

    #%%    
    
    # get sun
    def getSunAltitude(self):
        return self.inputJson['sun']['altitude']

    def getSunAzimuth(self):
        return self.inputJson['sun']['azimuth']

    def getSunIntensity(self):
        return self.inputJson['sun']['intensity']
    
    def getSunColR(self):
        return self.inputJson['sun']['color']['red']

    def getSunColG(self):
        return self.inputJson['sun']['color']['green']
    
    def getSunColB(self):
        return self.inputJson['sun']['color']['blue']
    
    #%%
    
    # get sky
    def getSkyYaw(self):
        return self.inputJson['sky']['skyYaw']
    
    def getSkyLight(self):
        return self.inputJson['sky']['skyLight']

    def getcloudSize(self):
        return self.inputJson['sky']['cloudSize']
    
    def getcloudX(self):
        return self.inputJson['sky']['cloudOffset']['x']
    
    def getcloudY(self):
        return self.inputJson['sky']['cloudOffset']['y']
    
    def getcloudZ(self):
        return self.inputJson['sky']['cloudOffset']['z']
    
    # might need sky color and all that.
    
    #%%
    
    #%%
    
    # set MISC
    def setEXP(self, fl):
        self.inputJson['exposure'] = fl
    
    def setWopac(self, fl):
        self.inputJson['waterOpacity'] = fl
    
    def setWvis(self, fl):
        self.inputJson['waterVisibility'] = fl
    
    #%% Water Colour missing.
    
    #%%
    def setFogR(self, fl):
        self.inputJson['fogColor']['red'] = fl

    def setFogG(self, fl):
        self.inputJson['fogColor']['green'] = fl

    def setFogB(self, fl):
        self.inputJson['fogColor']['blue'] = fl
    
    def setFogDen(self, fl):
        self.inputJson['fogDensity'] = fl
    
    #%%
    # set camera
    #   position
    def setX(self, fl):
        self.inputJson['camera']['position']['x'] = fl

    def setY(self, fl):
        self.inputJson['camera']['position']['y'] = fl

    def setZ(self, fl):
        self.inputJson['camera']['position']['z'] = fl

    #   orientation

    def setRoll(self, fl):
        self.inputJson['camera']['orientation']['roll'] = fl
    
    def setPitch(self, fl):
        self.inputJson['camera']['orientation']['pitch'] = fl

    def setYaw(self, fl):
        self.inputJson['camera']['orientation']['yaw'] = fl

    #   other
    def setFoV(self, fl):
        self.inputJson['camera']['fov'] = fl
    
    def setDoF(self, fl):
        self.inputJson['camera']['dof'] = fl

    def setfocalOffset(self, fl):
        self.inputJson['camera']['focalOffset'] = fl

    #%%    
    
    # set sun
    def setSunAltitude(self, fl):
        self.inputJson['sun']['altitude'] = fl

    def setSunAzimuth(self, fl):
        self.inputJson['sun']['azimuth'] = fl

    def setSunIntensity(self, fl):
        self.inputJson['sun']['intensity'] = fl
    
    def setSunColR(self, fl):
        self.inputJson['sun']['color']['red'] = fl

    def setSunColG(self, fl):
        self.inputJson['sun']['color']['green'] = fl
    
    def setSunColB(self, fl):
        self.inputJson['sun']['color']['blue'] = fl
    
    #%%
    
    # set sky
    def setSkyYaw(self, fl):
        self.inputJson['sky']['skyYaw'] = fl
    
    def setSkyLight(self, fl):
        self.inputJson['sky']['skyLight'] = fl

    def setcloudSize(self, fl):
        self.inputJson['sky']['cloudSize'] = fl
    
    def setcloudX(self, fl):
        self.inputJson['sky']['cloudOffset']['x'] = fl
    
    def setcloudY(self, fl):
        self.inputJson['sky']['cloudOffset']['y'] = fl
    
    def setcloudZ(self, fl):
        self.inputJson['sky']['cloudOffset']['z'] = fl



    def setName(self, f):
        self.filename = f
        self.inputJson['name'] = f

    def saveToFile(self, filename):
        with open(filename, 'w+') as f:
            json.dump(self.inputJson, f)

    def __init__(self, name):
        self.filename = name
        inputJsonString = open(name).read()

        self.inputJson = json.loads(inputJsonString)
