We learned how to generate images with DALL-E 2 API and manipulate basic properties like size, aspect ratio, brightness, contrast, saturation, and hue. In this lesson, we will explore more advanced image manipulation techniques to create even more variations and artistic effects.

Before that we are going to start with the same steps which are importing our libraries and having our function that generates our prompts. 
```python
import os
import openai
import secret
from PIL import Image
from io import BytesIO
import requests

openai.api_key = secret.api_key

# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']
```
{Try it!}(python3 imageGen.py 1)
### Image setting up

One technique to create more complex images is by composing multiple images together. In this example, we will overlay a generated image of a moon on top of an image of a night sky.

First step we are going to get our function to generate the images and save them into new files.

```python
# Generate moon and night sky images
moon_image_url = generate_base_image('moon')
night_sky_image_url = generate_base_image('night sky with stars')

img_data = requests.get(moon_image_url).content
with open('moon_image.jpg', 'wb') as handler:
    handler.write(img_data)

img_data = requests.get(night_sky_image_url).content
with open('night_sky_image.jpg', 'wb') as handler:
    handler.write(img_data)

```
{Try it!}(python3 imageGen.py 2)

[Click here to refresh your moon image](close_file moon_image.jpg panel=1; open_file moon_image.jpg panel=1)
[Click here to refresh your night sky image](close_file night_sky_image.jpg panel=1; open_file night_sky_image.jpg panel=1)

If you don't like the pictures generated, generate them again. If you like one and not the other comment out the code generation for the one you want. If you are happy with both, please comment out the generation code so we don't have to waste time generating images again and saving them over the image you want.  At the end you should have something more or less like this :
```python
"""
# Generate moon and night sky images
moon_image_url = generate_base_image('moon')
night_sky_image_url = generate_base_image('night sky with stars')

img_data = requests.get(moon_image_url).content
with open('moon_image.jpg', 'wb') as handler:
    handler.write(img_data)

img_data = requests.get(night_sky_image_url).content
with open('night_sky_image.jpg', 'wb') as handler:
    handler.write(img_data)
"""
```
Now we are ready to combine our images.


{Check It!|assessment}(multiple-choice-144853477)
