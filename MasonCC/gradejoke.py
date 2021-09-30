import matplotlib.pyplot as plt
import imageio
import numpy as np

gif = imageio.get_reader('riddle.gif')
num_frames = len(gif)

for frame in gif:
    imgplot = plt.imshow(frame, cmap='gray')
    plt.show()