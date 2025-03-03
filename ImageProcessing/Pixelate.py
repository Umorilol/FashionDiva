#This file wile take an image and pixelate it using the pyxleate library
from skimage import io
from pyxelate import Pyx, Pal

#load iamge with 'skimage.io.imread()'
image = io.imread('.venv\images\output.png')

downsample_by = 20 # new image will be 1/14th of the original
palette = 10 # find 7 colors

# 1) Instantiate Pyx Transformer
pyx = Pyx(factor=downsample_by, palette=palette)

#2) fit an image, allow Pyxelate to learn the color palette
pyx.fit(image)

#3 transform image to pixel art using the learned color palette
new_image = pyx.transform(image)

# save new image with 'skimage.io.imsave()'
io.imsave('.venv\images\pixel_sweatshirt.png', new_image)