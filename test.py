import os
from PIL import Image, ImageFilter

def test_files_exist():
    assert os.path.exists('plane.png'), "plane.png doesn't exist. Make sure you have correctly saved the image."
    assert os.path.exists('enhanced_plane.png'), "enhanced_plane.png doesn't exist. Make sure you have correctly saved the edge-enhanced image."

def test_image_processing():
    img_original = Image.open('plane.png')
    img_enhanced = Image.open('enhanced_plane.png')

    # Create an edge-enhanced image from the original for testing
    img_test = img_original.filter(ImageFilter.EDGE_ENHANCE)

    assert img_original.size == img_enhanced.size, "The original image and the enhanced image should be the same size."
    assert img_original.format == img_enhanced.format, "The original image and the enhanced image should be in the same format."
    
    assert img_original != img_enhanced, "The enhanced image should be different from the original image. Make sure you've applied the edge enhance filter correctly."

    assert list(img_enhanced.getdata()) == list(img_test.getdata()), "The student's enhanced image does not match the test image. Make sure the edge enhance filter was applied correctly."

if __name__ == "__main__":
    test_files_exist()
    test_image_processing()
    print("All tests passed.")
