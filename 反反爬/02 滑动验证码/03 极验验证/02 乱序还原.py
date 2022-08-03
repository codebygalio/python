full_location_list = [{'x': -157, 'y': -58}, {'x': -145, 'y': -58}, {'x': -265, 'y': -58}, {'x': -277, 'y': -58},
                      {'x': -181, 'y': -58}, {'x': -169, 'y': -58}, {'x': -241, 'y': -58}, {'x': -253, 'y': -58},
                      {'x': -109, 'y': -58}, {'x': -97, 'y': -58}, {'x': -289, 'y': -58}, {'x': -301, 'y': -58},
                      {'x': -85, 'y': -58}, {'x': -73, 'y': -58}, {'x': -25, 'y': -58}, {'x': -37, 'y': -58},
                      {'x': -13, 'y': -58}, {'x': -1, 'y': -58}, {'x': -121, 'y': -58}, {'x': -133, 'y': -58},
                      {'x': -61, 'y': -58}, {'x': -49, 'y': -58}, {'x': -217, 'y': -58}, {'x': -229, 'y': -58},
                      {'x': -205, 'y': -58}, {'x': -193, 'y': -58}, {'x': -145, 'y': 0}, {'x': -157, 'y': 0},
                      {'x': -277, 'y': 0}, {'x': -265, 'y': 0}, {'x': -169, 'y': 0}, {'x': -181, 'y': 0},
                      {'x': -253, 'y': 0}, {'x': -241, 'y': 0}, {'x': -97, 'y': 0}, {'x': -109, 'y': 0},
                      {'x': -301, 'y': 0}, {'x': -289, 'y': 0}, {'x': -73, 'y': 0}, {'x': -85, 'y': 0},
                      {'x': -37, 'y': 0}, {'x': -25, 'y': 0}, {'x': -1, 'y': 0}, {'x': -13, 'y': 0},
                      {'x': -133, 'y': 0}, {'x': -121, 'y': 0}, {'x': -49, 'y': 0}, {'x': -61, 'y': 0},
                      {'x': -229, 'y': 0}, {'x': -217, 'y': 0}, {'x': -193, 'y': 0}, {'x': -205, 'y': 0}]
cut_location_list = [{'x': -157, 'y': -58}, {'x': -145, 'y': -58}, {'x': -265, 'y': -58}, {'x': -277, 'y': -58},
                     {'x': -181, 'y': -58}, {'x': -169, 'y': -58}, {'x': -241, 'y': -58}, {'x': -253, 'y': -58},
                     {'x': -109, 'y': -58}, {'x': -97, 'y': -58}, {'x': -289, 'y': -58}, {'x': -301, 'y': -58},
                     {'x': -85, 'y': -58}, {'x': -73, 'y': -58}, {'x': -25, 'y': -58}, {'x': -37, 'y': -58},
                     {'x': -13, 'y': -58}, {'x': -1, 'y': -58}, {'x': -121, 'y': -58}, {'x': -133, 'y': -58},
                     {'x': -61, 'y': -58}, {'x': -49, 'y': -58}, {'x': -217, 'y': -58}, {'x': -229, 'y': -58},
                     {'x': -205, 'y': -58}, {'x': -193, 'y': -58}, {'x': -145, 'y': 0}, {'x': -157, 'y': 0},
                     {'x': -277, 'y': 0}, {'x': -265, 'y': 0}, {'x': -169, 'y': 0}, {'x': -181, 'y': 0},
                     {'x': -253, 'y': 0}, {'x': -241, 'y': 0}, {'x': -97, 'y': 0}, {'x': -109, 'y': 0},
                     {'x': -301, 'y': 0}, {'x': -289, 'y': 0}, {'x': -73, 'y': 0}, {'x': -85, 'y': 0},
                     {'x': -37, 'y': 0}, {'x': -25, 'y': 0}, {'x': -1, 'y': 0}, {'x': -13, 'y': 0}, {'x': -133, 'y': 0},
                     {'x': -121, 'y': 0}, {'x': -49, 'y': 0}, {'x': -61, 'y': 0}, {'x': -229, 'y': 0},
                     {'x': -217, 'y': 0}, {'x': -193, 'y': 0}, {'x': -205, 'y': 0}]
from PIL import Image

"""还原大图"""
full_image = Image.open('full_image.jpg')

new_im = Image.new('RGB', (260, 116))

# 把无序的图片 切成52张小图片
im_list_upper = []
im_list_down = []
# print(location_list)
for location in full_location_list:
    # print(location['y'])
    if location['y'] == -58:  # 上半边
        # 浏览器显示是负坐标系
        # full_image.crop 剪切图片
        im_list_upper.append(full_image.crop((abs(location['x']), 58, abs(location['x']) + 10, 116)))
    if location['y'] == 0:  # 下半边
        im_list_down.append(full_image.crop((abs(location['x']), 0, abs(location['x']) + 10, 58)))

x_offset = 0
for im in im_list_upper:
    # 把小图片放到 新的空白图片上
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

x_offset = 0
for im in im_list_down:
    new_im.paste(im, (x_offset, 58))
    x_offset += im.size[0]

new_im.save('full_images2.png')


"""还原小图"""
cut_image = Image.open('cut_image.jpg')
new_im = Image.new('RGB', (260, 116))
im_list_upper = []
im_list_down = []
# print(location_list)
for location in cut_location_list:
    # print(location['y'])
    if location['y'] == -58:  # 上半边
        im_list_upper.append(cut_image.crop((abs(location['x']), 58, abs(location['x']) + 10, 116)))
    if location['y'] == 0:  # 下半边
        im_list_down.append(cut_image.crop((abs(location['x']), 0, abs(location['x']) + 10, 58)))

x_offset = 0
for im in im_list_upper:
    new_im.paste(im, (x_offset, 0))  # 把小图片放到 新的空白图片上
    x_offset += im.size[0]

x_offset = 0
for im in im_list_down:
    new_im.paste(im, (x_offset, 58))
    x_offset += im.size[0]

new_im.save('cut_images2.png')
