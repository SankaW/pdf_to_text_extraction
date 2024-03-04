from PIL import Image
import pytesseract

# This is the path where you've installed Tesseract on your PC
# For example, on Windows, you might have it at:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#C:\Program Files\Tesseract-OCR

# Replace the path below with the path to the image you want to process
image_path = 'images/page_1.png'

# Open the image with Pillow
image = Image.open(image_path)

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(image)

print(text)


