from __future__ import division
import numpy as np
import time
import cv2
from SparkVideoReader import  SparkVideoReader


location = 'Dataset/alice.avi'


SparkReader = SparkVideoReader(location)

nrframes = SparkReader.getTotalFrames()
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
frameSize = SparkReader.getSize()
zeros = None
writer = cv2.VideoWriter('Output/test.avi', fourcc, 50, (frameSize[1], frameSize[0]), True)


for i in range(nrframes):
    frame = SparkReader.getFrame(i)
    writer.write(frame)


writer.release()
