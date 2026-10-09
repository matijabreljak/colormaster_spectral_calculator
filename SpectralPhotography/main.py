import rawpy
import math
import numpy as np
from PIL import Image
paths = ["C:/Users/Lenovo/Documents/GitHub/colormaster_spectral_calculator/SpectralPhotography/P1122520.RW2",
        # ... add more paths as needed
       ]
#run
#photos folder path dialog box
def DownsampleGreen(G1, G2):
    return (G1 + G2) / 2

def SaveChannelToCsv(channel, filename):
    np.savetxt(filename, channel, delimiter=",", fmt='%d')

def SelectAndImportFolder(paths):
    return
def SelectAndExportFolder(channels):
    return

for i in range(len(paths)):
    with rawpy.imread(paths[i]) as raw:
        rgb = raw.raw_image_visible.astype(np.float32)
        R=rgb[0::2, 0::2]
        B=rgb[1::2, 1::2] 
        G=(rgb[0::2, 1::2] + rgb[1::2, 0::2])/2
        SaveChannelToCsv(R, "R"+str(i))
        SaveChannelToCsv(G, "G"+str(i))
        SaveChannelToCsv(B, "B"+str(i))



