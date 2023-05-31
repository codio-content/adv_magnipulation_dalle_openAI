#CODIO SOLUTION BEGIN
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
moon_image=Image.open('moon_image.jpg')
night_sky_image=Image.open('night_sky_image.jpg')
# Resize the moon image to fit the composition
moon_image = moon_image.resize((200, 200), Image.ANTIALIAS)
# Overlay the moon image on top of the night sky image
# Overlay the moon image on top of the night sky image
if moon_image.mode in ('RGBA', 'LA') or (moon_image.mode == 'P' and 'transparency' in moon_image.info):
    night_sky_image.paste(moon_image, (0, 0), moon_image)
else:
    night_sky_image.paste(moon_image, (0, 0))

# Save the composed image to a file
night_sky_image.save('night_sky_with_moon.jpg')

#CODIO SOLUTION END
