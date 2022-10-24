import os, glob
from PIL import Image, ImageOps
from colorthief import ColorThief


input_dir = "input_images"
output_dir = "output_images"

for filepath in glob.iglob(f"{input_dir}/*.png"):
  if filepath.endswith(".png"):
    filename = filepath.lower().replace("/", "").replace("\\", "").replace(input_dir, "").replace(".png", ".jpg")
    print(f"Converting {filepath}...")
    color_thief = ColorThief(filepath)
    dominant_color = color_thief.get_color(quality=1)
    
    image = Image.open(filepath).convert("RGBA")
    
    new_image = Image.new("RGB", image.size, dominant_color) # background color image
    new_image = ImageOps.invert(new_image)
    new_image = new_image.convert("RGBA")
    new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
    new_image.convert('RGB').save(f'{output_dir}/{filename}', "JPEG")  # Save as JPEG
    print(f"Converted {filename}!")
print("Processing complete!")
exit()