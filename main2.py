import PIL.Image as Image
import pytesseract

# Open the image
image = Image.open('modified/Im1.jpg')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

height, width = image.size

left_top_img = image.crop((205, 469, 1225, 1273))
right_top_img = image.crop((1225, 469, 2245, 1273))
right_bottom_img = image.crop((1225, 1767, 2245, 2700))
left_bottom_img = image.crop((205, 1767, 1225, 2700))

