from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt

# Load image
img = Image.open("your_image.jpg")
img.show()

# Plot in console
plt.imshow(img)
plt.axis('off')
plt.show()

# Display size
print("Original Size:", img.size)

# Resize to half
half_img = img.resize((img.width // 2, img.height // 2))
half_img.show()

# Rotate 145 degrees
rotated_img = img.rotate(145)
rotated_img.show()

# Resize to 50x70
resized_img = img.resize((50, 70))
resized_img.show()

# Flip left-right and top-bottom
flipped_lr = ImageOps.mirror(img)
flipped_lr.show()
flipped_tb = ImageOps.flip(img)
flipped_tb.show()

# Crop (example: center square crop)
width, height = img.size
crop_area = (width//4, height//4, width*3//4, height*3//4)
cropped_img = img.crop(crop_area)
cropped_img.show()

# Convert to grayscale and black & white
gray_img = img.convert("L")
gray_img.show()
bw_img = img.convert("1")
bw_img.show()

# Apply blur
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.show()
