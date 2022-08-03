from PIL import Image


def binarizing(img, threshold):
    """传入image对象进行灰度、二值处理"""
    img = img.convert("L")  # 转灰度
    img.save('binarizing_gray.png')

    pix_data = img.load()
    w, h = img.size
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pix_data[x, y] < threshold:
                pix_data[x, y] = 0
            else:
                pix_data[x, y] = 255
    img.save('binarizing.png')
    return img


image = Image.open('captcha.png')
binarizing(image, 140)
