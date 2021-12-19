from PIL import Image, ImageDraw
from numpy import genfromtxt

g = open('Record_2021-12-03_12-29-32.csv', 'r')
temp = genfromtxt(g, delimiter=',')
im = Image.fromarray(temp).convert('RGB')
pix = im.load()
rows, cols = im.size
for x in range(cols):
    for y in range(rows):
        print(str(x) + " " + str(y))
        pix[x, y] = (int(temp[y, x] // 256 // 256 % 256), int(temp[y, x] // 256 % 256), int(temp[y, x] % 256))
im.save(g.name[0:-4] + '.jpeg')
