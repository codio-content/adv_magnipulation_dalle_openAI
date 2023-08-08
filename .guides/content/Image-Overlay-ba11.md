### Image composition 
The first step is to  open our saved images as variables. 
```python
moon_image=Image.open('moon_image.jpg')
night_sky_image=Image.open('night_sky_image.jpg')
```
{Try it!}(python3 imageGen.py 6)
[Click here to refresh your moon image](close_file moon_image.jpg panel=1; open_file moon_image.jpg panel=1)
[Click here to refresh your night sky image](close_file night_sky_image.jpg panel=1; open_file night_sky_image.jpg panel=1)

The next step is to resize our images. 
```
# Resize the moon image to fit the composition
moon_image = moon_image.resize((200, 200), Image.ANTIALIAS)
```
{Try it!}(python3 imageGen.py 5)
Resize the moon image: The `resize()` function is used to change the size of the moon image. The target size is specified as a tuple of (width, height), which in this case is `(200, 200)`. The `Image.ANTIALIAS` parameter is used to apply a high-quality downsampling filter that smooths out the image when resizing.

```python
# Overlay the moon image on top of the night sky image
night_sky_image.paste(moon_image, (150, 100), moon_image)
```
{Try it!}(python3 imageGen.py 4)

Overlay the moon image on the night sky image: The `paste()` function is used to overlay the moon image on top of the night sky image. The function takes three arguments: the image to paste `moon_image`, the position where the pasted image should be placed (specified as an `(x, y)` tuple), and an optional `mask` (`moon_image` in this case). The mask is used to preserve transparency in the pasted image, which is important when overlaying images with transparent backgrounds. If an error was generated please read the note section, otherwise you can continue to the save image section.


**Please note**: if you get a bad transparency mask error, it is because the image you are trying to paste does not have an alpha channel. An **alpha channel** is a layer of transparency information that is stored in an image file. It allows parts of the image to be transparent, so that other images can be seen behind them.

In your code, you are trying to paste the moon image onto the night sky image, but the moon image does not have an alpha channel. This means that the Python Imaging Library (PIL) does not know how to blend the two images together, and it throws an error.

To fix this error, you need to convert the moon image to a format that supports alpha channels. You can do this using a graphics editing program like Photoshop or GIMP. We will do it using the `convert(“RGBA”)` function. Once you have converted the moon image, you can paste it onto the night sky image without any errors.
```python
# Convert the moon image to RGBA format
moon_image = moon_image.convert("RGBA")

# Paste the moon image onto the night sky image
night_sky_image.paste(moon_image, (150, 100), moon_image)

```
**Now we need to save our new image**
```python
# Save the composed image to a file
night_sky_image.save('night_sky_with_moon.jpg')
```
Save the composed image to a file: The `save()` function is used to save the composed image to a file. The file name is specified as a string (`night_sky_with_moon.jpg`), and the image will be saved in the same folder as your script.

{Try it!}(python3 imageGen.py 2)

[Click here to refresh your night sky with moon image](close_file night_sky_with_moon.jpg panel=1; open_file night_sky_with_moon.jpg panel=1)

Here is another approach to check the mode of the `moon_image` variable. Firstly, we check if it is in the right format. If it is so, we paste the image. Else we convert it to ` “RGBA” ` and then run the `paste` function.
```python
# Overlay the moon image on top of the night sky image
if moon_image.mode in ('RGBA', 'LA') or (moon_image.mode == 'P' and 'transparency' in moon_image.info):
    night_sky_image.paste(moon_image, (150, 100))
else:
    moon_image = moon_image.convert("RGBA")
    night_sky_image.paste(moon_image, (150, 100))
```
{Try it!}(python3 imageGen.py 3)

[Click here to refresh your night sky with moon image](close_file night_sky_with_moon.jpg panel=1; open_file night_sky_with_moon.jpg panel=1)

If for example you wanted the image at the top right corner it would be `(0,0)` , you can play around with the coordinates so it fits your image better. 
Depending on your image for now, you will basically see an overlay of your moon into your night sky. In most cases, using this method transparency will not work that well. 

{Check It!|assessment}(multiple-choice-2011872140)

