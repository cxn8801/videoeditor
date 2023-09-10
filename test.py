import pytesseract
from PIL import Image
img = Image.open("8.png")
text = pytesseract.image_to_string(img, lang='chi_sim+eng')
print(text)