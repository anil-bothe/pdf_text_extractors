import json
import PyPDF2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import os, sys


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# extracting images
pdf_reader = PyPDF2.PdfReader('pdf/CIA DOcs_0003.pdf')
images = []
for page in pdf_reader.pages:
    for image in page.images:
        with open(f"images/{image.name}", "wb") as f:
            f.write(image.data)

print("Image extraction done.")


# apply filter to images
output = []
files = os.listdir('images')
files.sort()
count = 0
for file in files:
    count += 1
    sys.stdout.write('\r')
    p = round(count/len(pdf_reader.pages) * 100)

    im = Image.open(f"images/{file}")
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('L')
    im = im.point(lambda p: 255 if p > 128 else 0)

    height, width = im.size

    left_top_img = im.crop((150, 445, 1213, 1273))
    right_top_img = im.crop((1213, 445, 2245, 1273))
    right_bottom_img = im.crop((1213, 1730, 2245, 2700))
    left_bottom_img = im.crop((150, 1730, 1213, 2700))

    data_dict = {
        "left_top_img": pytesseract.image_to_string(left_top_img),
        "right_top_img": pytesseract.image_to_string(right_top_img),
        "right_bottom_img": pytesseract.image_to_string(right_bottom_img),
        "left_bottom_img": pytesseract.image_to_string(left_bottom_img),
    }

    left_top_img.save("out/1"+ file)
    right_top_img.save("out/2"+ file)
    right_bottom_img.save("out/3"+ file)
    left_bottom_img.save("out/4"+ file)

    output.append(data_dict)
    sys.stdout.write("[%-100s] %d%%" % ('='*p, p))
    sys.stdout.flush()

with open('x.json', "w") as f:
    json.dump(output, f, indent=4)
