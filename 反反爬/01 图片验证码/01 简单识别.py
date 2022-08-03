import pytesseract
# pillow 安装的库名与导入的包名是不一样的
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 1 加载图片
image = Image.open('test.png')
# 2. 识别图片上的文字
string = pytesseract.image_to_string(image)
# 3. 打印识别的文字
print(string)
