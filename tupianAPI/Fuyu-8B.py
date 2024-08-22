import os
import qianfan
import base64
from qianfan.resources import Image2Text

# 设置 QIANFAN API 的访问密钥
os.environ["QIANFAN_ACCESS_KEY"] =""
os.environ["QIANFAN_SECRET_KEY"] =""

# 请替换图片对应的路径地址
with open(r"D:\pythoncode\qf\tupianAPI\8.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# 使用model参数
i2t = Image2Text(model="Fuyu-8B")
resp = i2t.do(prompt="分析一下图片画了什么", image=encoded_string)

print(resp["result"])
