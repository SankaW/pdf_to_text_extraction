import cv2
import pytesseract
import csv

# Replace with your Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_csv(year):
    image_path = f'C:\Educational\Sri Lanka Data\childprotection.gov.lk\child_protection_data\data\Images\District_wise\{year}.png'

    # Load the image
    img = cv2.imread(image_path)

    # Preprocess the image (optional)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding (adjust threshold value as needed)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

    # Extract text using OCR
    text = pytesseract.image_to_string(thresh)

    # Parse and structure the data (replace with your logic)
    # This is a basic example, you might need to adapt it to your specific table format
    lines = text.split('\n')
    data = []
    for line in lines:
        # Split each line based on a delimiter (e.g., tab, comma)
        data.append(line.split('\t'))

    csv_file_path = f'CSV/{year}_district_wise_reported_case.csv'
    # Write data to CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    print(f'{year} CSV file created successfully!')


for year in range(2016,2022):
    image_to_csv(year)