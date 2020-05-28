from PIL import Image
import subprocess
import os

catIm = Image.open('data/zophie.jpg')
print(catIm.size)
width, height = catIm.size
print(width)
print(height)


print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
catIm.save('data/zoophie.png')

catIm.crop((50,75,75,100)).save('data/zoophie_crop.png')


catIm.resize((width, height+300)).save('data/zoophie_svelt.png')

# Image.new('RGBA', (100,100), 'red').save('data/red_array.png')