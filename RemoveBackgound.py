#This file will use rembg to remove the background of a photo 
from rembg import remove
from PIL import Image

input_path = '.venv\images\input.png'
output_path = '.venv\images\output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)