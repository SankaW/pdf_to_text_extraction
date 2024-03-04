import fitz  # PyMuPDF is imported as fitz
from PIL import Image, ImageEnhance
import io

year = 2022
# Define the path to your PDF file
pdf_path = f'C:\Educational\Sri Lanka Data\childprotection.gov.lk\child_protection_data\data\Statistical_data_-_Year_{year}.pdf'

pdf_document = fitz.open(pdf_path)

for page_number in range(len(pdf_document)):
    page = pdf_document[page_number]
    zoom = 2  # 2x zoom for a higher resolution
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)

    # Store the image in memory
    image_bytes = pix.tobytes("ppm")
    image = Image.open(io.BytesIO(image_bytes))

    # Apply image processing to improve OCR results
    # Convert the image to grayscale
    image = image.convert('L')

    # Enhance the contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)

    image_path = f'images/page_{year}_{page_number + 1}.png'
    image.save(image_path)

pdf_document.close()
