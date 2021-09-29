from PIL import Image
import imageio
import qrtools

gif = imageio.get_reader('riddle.gif')
print(gif)
num_frames = len(gif)

for frame in gif:
    f1 = Image.fromarray(frame)
    qr = qrtools.QR()
    qr.decode(f1)
    print(qr.data)
    print(frame)