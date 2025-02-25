from rembg import remove
from PIL import Image
from skimage import io
from pyxelate import Pyx, Pal

input_path = '.venv\images\input.png'
output_path = '.venv\images\output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

#load iamge with 'skimage.io.imread()'
image = io.imread('.venv\images\output.png')

downsample_by = 10 # new image will be 1/14th of the original
palette = 7 # find 7 colors

# 1) Instantiate Pyx Transformer
pyx = Pyx(factor=downsample_by, palette=palette)

#2) fit an image, allow Pyxelate to learn the color palette
pyx.fit(image)

#3 transform image to pixel art using the learned color palette
new_image = pyx.transform(image)

# save new image with 'skimage.io.imsave()'
io.imsave('.venv\images\pixel_sweatshirt.png', new_image)