import pytesseract # type: ignore
import cv2 # type: ignore
import re
import json


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_lab_data(image_path):
 
    img = cv2.imread(image_path)

    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)


    text = pytesseract.image_to_string(thresh)

    pattern = r'(?P<test_name>.+?)\s+(?P<value>\d+\.?\d*)\s+(?P<unit>[a-zA-Z/%]+)?\s+(?P<low>\d+\.?\d*)\s*-\s*(?P<high>\d+\.?\d*)'
    results = []

   
    for match in re.finditer(pattern, text):
        try:
            name = match.group("test_name").strip()
            value = float(match.group("value"))
            unit = match.group("unit") or ""
            low = float(match.group("low"))
            high = float(match.group("high"))
            out_of_range = not (low <= value <= high)

            
            results.append({
                "test_name": name,
                "test_value": str(value),
                "bio_reference_range": f"{low}-{high}",
                "test_unit": unit,
                "lab_test_out_of_range": out_of_range
            })
        except Exception as e:
            continue

    return {
        "is_success": True,
        "data": results
    }

if __name__ == "__main__":
    
    image_file = r"C:\Users\Shubham\Desktop\Bajaj Finserv round 2\lbmaske\AHD-0425-PA-0007719_E-REPORTS_250427_2032@E.pdf_page_7.png"
    
    
    output = extract_lab_data(image_file)
    
    
    print(json.dumps(output, indent=2))
