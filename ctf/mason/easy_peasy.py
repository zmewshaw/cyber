import sys
from PIL import Image

img_list = []
for i in range(30):
    img_list.append(str(i) + ".png")

images = [Image.open(x) for x in img_list]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
total_height = heights[0]

new_image = Image.new('1', (total_width, total_height))

x = 0
for im in images:
    new_image.paste(im, (x, 0))
    x += im.size[0]

new_image.save('test.png')