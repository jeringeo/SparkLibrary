import numpy as np
import os.path

saveFolder = '/home/jerin/JerinsCloud/Phd/Acads/Research/Autum2017/ImageReconstruction/SavedData/'

def save(variable,fileName):
    np.save(saveFolder+fileName+'.npy',variable)

def load(fileName):
    fileName = saveFolder+fileName+'.npy'
    if(os.path.isfile(fileName)==False):
        return None

    variable = np.array(np.load(fileName))
    return variable