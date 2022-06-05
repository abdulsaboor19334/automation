import cv2
import pytesseract
from pdf2image import convert_from_path

config = ('-l eng --oem 1 --psm 3')
# pages = convert_from_path('pdfs/img.pdf')
# pages[0].save('images/out.png','PNG')



img = cv2.imread('images/out.png')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(grey,5)
retval, img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

text = pytesseract.image_to_string(img, config=config)
with open('data.txt','w') as f:
    f.write(text)

print(text)