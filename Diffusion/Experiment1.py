from diffusers import StableDiffusionPipeline
from PIL import Image


classes = ["hammer", "cat", "banana", "guitar"]  # Each is a cluster
images_per_class = 4 


from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda")

generated_images = {}
for cls in classes:
    generated_images[cls] = [pipe(f"A photo of a {cls}").images[0] for _ in range(images_per_class)]

from PIL import Image

cols = 4
rows = len(classes)
grid_img = Image.new("RGB", (cols * 128, rows * 128))

for row, cls in enumerate(classes):
    for col, img in enumerate(generated_images[cls]):
        grid_img.paste(img.resize((128, 128)), (col * 128, row * 128))
grid_img.save("generated_images.png")
grid_img.show()
import numpy as np
from diffusers import StableDiffusionPipeline
from PIL import Image


solution_map = []
for i, cls in enumerate(classes):
    for j in range(images_per_class):
        solution_map.append({
            "row": i, "col": j, "label": cls
        })
print(solution_map)
