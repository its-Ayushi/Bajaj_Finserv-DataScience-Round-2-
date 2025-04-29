
# 🧪 Lab Report Data Extraction using OCR | Bajaj Finserv Round 3

This project automates the extraction of structured lab test data from scanned medical report images using **Tesseract OCR** and **OpenCV** in Python. It identifies test values, units, reference ranges, and whether a result is out of range.

---

## 📌 Objective

To streamline the interpretation of lab reports by:
- Converting image-based lab reports into structured digital data.
- Extracting relevant information such as test name, value, unit, and biological reference range.
- Detecting whether each test result falls within the normal range.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Tesseract OCR**
- **OpenCV**
- **pytesseract**
- **Regular Expressions**
- **JSON for structured output**

---

## 🧰 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/lab-report-ocr.git
cd lab-report-ocr
```

### 2. Install Python dependencies
```bash
pip install opencv-python pytesseract
```

### 3. Install Tesseract OCR

Download and install from:  
👉 [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)


---

## 📂 Dataset Reference

Sample lab report images for testing are located in:  
```
Dataset link: https://drive.google.com/file/d/1LzG7oJ-cqGHK9KbwXnWfkWgnQ3xi8Cr9/view?usp=sharing
```

You can extract and test on any `.png` or `.jpg` file inside the zip archive.

---

## 🚀 How to Run

### 1. Update the image path in `lab.py`:
```python
image_file = r"C:\path\to\your\image.png"
```

### 2. Run the script
```bash
python lab.py
```

---

## 📤 Sample Output

```json

{
  "is_success": true,
  "data": [
    {
      "test_name": "Mean Corpuscular Volume (M.C.V.) :",
      "test_value": "88.3",
      "bio_reference_range": "83.0-95.0",
      "test_unit": "fl",
      "lab_test_out_of_range": false
    },
    {
      "test_name": "Mean Corpuscular Hb (M.C.H.) :",
      "test_value": "28.5",
      "bio_reference_range": "27.0-32.0",
      "test_unit": "Pg",
      "lab_test_out_of_range": false
    },
    {
      "test_name": "Basophils :",
      "test_value": "0.2",
      "bio_reference_range": "0.0-1.0",
      "test_unit": "%",
      "lab_test_out_of_range": false
    },
    {
      "test_name": "@ Platelet Count :",
      "test_value": "870.0",
      "bio_reference_range": "150.0-450.0",
      "test_unit": "dul",
      "lab_test_out_of_range": true
    },
    {
      "test_name": "' {#}MPV :",
      "test_value": "9.4",
      "bio_reference_range": "6.78-13.46",
      "test_unit": "fL",
      "lab_test_out_of_range": false
    },
    {
      "test_name": "{ #} IMMATURE PLATELET FRACTION :",
      "test_value": "2.9",
      "bio_reference_range": "0.0-5.0",
      "test_unit": "%",
      "lab_test_out_of_range": false
    },
    {
      "test_name": "Eosinophils (abs) :",
      "test_value": "73.92",
      "bio_reference_range": "0.0-400.0",
      "test_unit": "ful",
      "lab_test_out_of_range": false
    },
    {
      "test_name": "Monocytes (abs) :",
      "test_value": "80.8",
      "bio_reference_range": "0.0-1000.0",
      "test_unit": "ful",
      "lab_test_out_of_range": false
    }
  ]
}
```

---

## 📁 File Structure

```
.
├── lab.py                    # Main script to run OCR and extract data
├── README.md                 # Project documentation
├── lab_reports_samples.zip   # Sample image dataset (stored locally)
```

---

## 🧑‍💻 Author

**Ayushi Agarwal**  
Submitted as part of **Bajaj Finserv Round 3**  
April 2025

---

## 📜 License

This project is licensed for educational and internal evaluation purposes.
