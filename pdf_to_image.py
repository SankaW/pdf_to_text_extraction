import fitz  # PyMuPDF is imported as fitz

pdf_document = fitz.open(r'C:\Educational\Sri Lanka Data\childprotection.gov.lk\child_protection_data\data\Statistical_data_-_Year_2010.pdf')

for page_number in range(len(pdf_document)):
    page = pdf_document[page_number]
    zoom = 2  # 2x zoom for a higher resolution
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    image_path = f'images/page_{page_number + 1}.png'
    pix.save(image_path)

pdf_document.close()
