from PIL import Image
import imageio
import qrtools

gif = imageio.get_reader('riddle.gif')
num_frames = len(gif)

for frame in gif:
    print(frame)