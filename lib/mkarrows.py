from PIL import Image
import os

im = Image.open("../static/arrow.png")

os.makedirs('../static/arrows')

for i in range(0,361):
	im.rotate(i).save("../static/arrows/arrow"+ str(i)+".png")
