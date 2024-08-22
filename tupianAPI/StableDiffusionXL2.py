import os
import qianfan
from PIL import Image
import io

os.environ["QIANFAN_ACCESS_KEY"] =""
os.environ["QIANFAN_SECRET_KEY"] =""

# 创建 Completion 和 Text2Image 的实例
comp = qianfan.Completion()
t2i = qianfan.Text2Image()

# 用户输入中文商品描述
user_keywords =input("请输入中文商品描述：")

# 调用 Completion API 生成英文商品描述
resp_desc = comp.do(
    prompt=f"根据以下中文关键词生成详细的英文商品描述（请限制在250个单词以内）: {user_keywords}\n\nKeywords: {user_keywords}\nEnglish Description:",
)

# 获取英文描述
english_description = resp_desc.body["result"]
print(english_description)

# 调用 Text2Image API 生成基于英文描述的图片
resp_img = t2i.do(
    prompt=f"A product image based on the following description: {english_description}.",
    with_decode="base64"
)

# 获取 Base64 编码的图像数据
img_data = resp_img["body"]["data"][0]["image"]

# 解码 Base64 图像数据
img = Image.open(io.BytesIO(img_data))
img.show()