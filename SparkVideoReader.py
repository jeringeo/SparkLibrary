from __future__ import division
import cv2 as opencv
import hashlib
import numpy as np
import SparkHashing
import  os

class SparkVideoReader:

    filePath = None
    md5Sum = []
    captureAgent = None
    nrFrames = 0
    fps = 0

    width = 0
    height = 0


    def  __init__(self, fileName):
        cap = opencv.VideoCapture(fileName)
        self.filePath = fileName
        self.captureAgent = cap
        self.nrFrames = int(cap.get(opencv.CAP_PROP_FRAME_COUNT))
        self.width = int(cap.get(opencv.CAP_PROP_FRAME_WIDTH))
        self.height = int(cap.get(opencv.CAP_PROP_FRAME_HEIGHT))
        self.fps = cap.get(opencv.CAP_PROP_FPS)
        self.md5Sum = SparkHashing.getHashOfFile(fileName)

    def getTotalFrames(self):
        return self.nrFrames

    def getSize(self):
        return self.height, self.width

    def getFrame(self,frameIndex):
        if(int(self.captureAgent.get(opencv.CAP_PROP_POS_FRAMES))!=frameIndex):
          self.captureAgent.set(1,frameIndex)

        ret, frame = self.captureAgent.read()
        #frame = convertToGray(frame)
        return frame

    def getChannels(self):
        frame = self.getFrame(0)
        shape = frame.shape
        if(len(shape)==2):
            return 1
        else:
            return shape[2]

    def getFPS(self):
        return self.fps

    def close(self):
        self.captureAgent.release()

    def count_frames_manual(self,video):
        total = 0

        while True:
            (grabbed, frame) = video.read()
            if not grabbed:
                break
            total += 1

        return total

    def getMD5Sum(self):
        return self.md5Sum

    def getFileName(self):
        name = os.path.basename(self.filePath)
        return name

    def getUniqueID(self):
        name = self.getFileName().split('.')[0]
        fileHash = self.getMD5Sum()
        uid = name + '_' + fileHash
        return uid

def convertToGray(image):
    if(len(image.shape) == 3):
        image = opencv.cvtColor(image, opencv.COLOR_RGB2GRAY)

    return image

