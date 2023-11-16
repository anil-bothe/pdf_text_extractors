import json
import PyPDF2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import os
import sys

# extracting images
pdf_reader = PyPDF2.PdfReader('pdf/HIGH COURT DIRECTORY PDF 2023 (1).pdf')
arr = []

count = 0
for page in pdf_reader.pages:
    count += 1
    sys.stdout.write('\r')
    p = round(count/len(pdf_reader.pages) * 100)
    sys.stdout.write("[%-100s] %d%%" % ('='*p, p))
    sys.stdout.flush()
    
    # skip pages
    if (count < 2 and count > 177):
        continue

    arr.append(page.extract_text())

with open("high-court.json", "w") as f:
    json.dump(arr, f, indent=4)
