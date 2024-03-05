from PIL import Image, ImageFilter
import pytesseract

# This is the path where you've installed Tesseract on your PC
# For example, on Windows, you might have it at:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Improve image quality by converting to grayscale and increasing contrast
def preprocess_image(image_path):
    # Open the image with Pillow
    image = Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale
    image = image.point(lambda x: 0 if x < 140 else 255)  # Binarization
    image = image.filter(ImageFilter.SMOOTH_MORE)  # Smooth the image
    return image

# Replace the path below with the path to the image you want to process
image_path = 'images/2022_ChildProtectionCases_district.png'
#year = 2022
#image_path = f'C:\Educational\Sri Lanka Data\childprotection.gov.lk\child_protection_data\data\Images\District_wise\{year}.png'

# Preprocess the image
image = preprocess_image(image_path)

# Use pytesseract to do OCR on the image
# Specify the Tesseract options
#custom_config = r'--oem 3 --psm 6 --user-words user_words.txt'
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(image, config=custom_config)

print(text)


