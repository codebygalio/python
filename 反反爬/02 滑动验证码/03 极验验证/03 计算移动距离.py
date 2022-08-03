from PIL import Image

full_image = Image.open('full_images2.png')
cut_image = Image.open('cut_images2.png')
# print('size', image1.size)
# rgb的差值不超过这一个范围 误差范围
threshold = 50
for i in range(0, full_image.size[0]):  # 260
    for j in range(0, full_image.size[1]):  # 160
        pixel1 = full_image.getpixel((i, j))
        pixel2 = cut_image.getpixel((i, j))
        # 对比每一个点的三原色
        res_R = abs(pixel1[0] - pixel2[0])  # 计算RGB差
        res_G = abs(pixel1[1] - pixel2[1])  # 计算RGB差
        res_B = abs(pixel1[2] - pixel2[2])  # 计算RGB差
        if res_R > threshold and res_G > threshold and res_B > threshold:
            print(i, j)
            exit()
