Now we will explore how to apply various image filters to images generated by the DALL-E 2 API using the Python Imaging Library (PIL). Image filters can be used to enhance, stylize, or transform your images, creating unique and visually striking results.

For now we are going to go back to our apple example. 
```python

# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']
base_image_url = generate_base_image('red apple')


img_data = requests.get(base_image_url).content
with open('base_apple.jpg', 'wb') as handler:
    handler.write(img_data)
```
{Try it!}(python3 ImageGen2.py 2)

[Click here to refresh your apple image](close_file base_apple.jpg panel=1; open_file base_apple.jpg panel=1)

Run it once to generate your "apple" then comment out the code so we have the base apple that we want to interact with. Your comment should more or less look like this 

```python-hide-clipboard
"""    
base_image_url = generate_base_image('red apple')


img_data = requests.get(base_image_url).content
with open('base_apple.jpg', 'wb') as handler:
    handler.write(img_data)
"""
```
The last step is saving our image as a variable so we can more easily interact with it. 
```
apple_image=Image.open('base_apple.jpg')
```
{Try it!}(python3 ImageGen2.py 3)

------
# PIL

The PIL library provides several built-in filters that you can apply to your images. These filters include blurring, sharpening, contouring, edge detection, and many others. We will explore some of these filters and learn how to apply them to images generated by the DALL-E 2 API.

#### Gaussian Blur

A Gaussian blur filter softens the image by reducing noise and details. This filter can be used to create a dreamy or ethereal effect, or to reduce noise in an image.

```python
from PIL import ImageFilter

# Apply a Gaussian blur filter to the base image
blurred_image = apple_image.filter(ImageFilter.GaussianBlur(radius=5))

# Save the blurred image to a file
blurred_image.save('blurred_red_apple.jpg')
```
{Try it!}(python3 ImageGen2.py 4)

[Click here to refresh your  blurred apple image](close_file blurred_red_apple.jpg panel=1; open_file blurred_red_apple.jpg panel=1)

#### Contour

The contour filter traces the edges of objects in the image, creating a high-contrast, black-and-white image that highlights the shapes in the scene.
```python
from PIL import ImageFilter

# Apply a contour filter to the base image
contour_image = apple_image.filter(ImageFilter.CONTOUR)

# Save the contour image to a file
contour_image.save('contour_red_apple.jpg')
```

{Try it!}(python3 ImageGen2.py 5)

[Click here to refresh your contour apple image](close_file contour_red_apple.jpg panel=1; open_file contour_red_apple.jpg panel=1)

{Check It!|assessment}(multiple-choice-1927310745)