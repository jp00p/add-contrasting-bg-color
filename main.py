import os, glob, random
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

input_dir = "input_images"
output_dir = "output_images"

for filepath in glob.iglob(f"{input_dir}/*.png"):
  if filepath.endswith(".png"):
    filename = filepath.lower().replace("/", "").replace("\\", "").replace(input_dir, "")
    print(f"Converting {filepath}...")
    random_color = (random.randint(45,255), random.randint(45,255), random.randint(45,255))
    image = Image.open(filepath).convert("RGBA")

    '''
    uncomment to replace a color (RGB) with transparency
    you can also do >= comparison on the color if you want to get fuzzy
    '''
    # pixdata = image.load()
    # width, height = image.size
    # for y in range(height):
    #     for x in range(width):
    #         if pixdata[x, y] == (0, 0, 0, 255):
    #             pixdata[x, y] = (255, 255, 255, 0)


    '''uncomment to crop image to the center'''
    # width, height = image.size
    # new_size = 64
    # left = (width - new_size)/2
    # top = (height - new_size)/2
    # right = (width + new_size)/2
    # bottom = (height + new_size)/2
    # image = image.crop((left, top, right, bottom))
 

    image = image.resize((512,512), Image.NEAREST)
    new_image = Image.new("RGB", image.size, random_color)
    new_image = ImageOps.invert(new_image)
    new_image = new_image.convert("RGBA")
    new_image.paste(image, (0, 0), image)
    new_image.convert('RGB').save(f'{output_dir}/{filename}', "PNG")
    print(f"Converted {filename}!")
print("Processing complete!")
exit()