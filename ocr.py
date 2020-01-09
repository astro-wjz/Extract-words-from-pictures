## 百度API精确识别并将文字输出在命令行，同时将文字保存在剪贴板中
## 使用前请仔细阅读说明文件

from PIL import Image
from PIL import ImageGrab
import os
import pyperclip
from aip import AipOcr

image = ImageGrab.grabclipboard()   # 从剪贴板中获取图片，若图片已经保存在某文件夹中，请注释掉第10行，第11行和第39行
image.save("capture.png")

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

print('----------------------------------------')

with open("capture.png", 'rb') as f:        # 若图片已存在，请填写文件实际路径
                                            # 例如 with open(r"C:\Users\name\Desktop\jietu.png", 'rb') as f:
    file = open("temp.txt", 'w+', encoding='utf-8')
    image = f.read()
    # 调用百度API通用文字识别（高精度版），提取图片中的内容
    # text = client.basicGeneral(image)     # 粗略识别
    text = client.basicAccurate(image)      # 精确识别，每日免费500次
    result = text["words_result"]
    for i in result:
        #print(i["words"])
        #file.write(i["words"] + '\n')      # 换行
        file.write(i["words"])              # 不换行
    file.close()
    file = open("temp.txt", 'r', encoding='utf-8')
    contents = file.read()
    print(contents)                         # 输出结果，并保存在文件 temp.txt 中
    pyperclip.copy(contents)                # 同时将结果存放在剪贴板中
    file.close()
os.remove("capture.png")                    # 移除图片文件
os.remove("temp.txt")                       # 移除结果文件

print('----------------------------------------' + '\n')
print('Finished !')
