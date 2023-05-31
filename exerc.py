import os
import openai
import secret
from PIL import Image, ImageFilter
from io import BytesIO
import requests
openai.api_key = secret.api_key

#CODIO SOLUTION BEGIN
# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

plane_url = generate_base_image('plane in flight')
img_data = requests.get(plane_url).content
with open('plane.png', 'wb') as handler:
    handler.write(img_data)

plane_image=Image.open('plane.png')
# Apply an edge enhance filter to the base image
edge_enhanced_image = plane_image.filter(ImageFilter.EDGE_ENHANCE)
# Save the edge enhanced image to a file
edge_enhanced_image.save('enhanced_plane.png')


#CODIO SOLUTION END