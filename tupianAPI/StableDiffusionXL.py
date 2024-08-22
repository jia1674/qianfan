import os
import qianfan
import io
from PIL import Image

os.environ["QIANFAN_ACCESS_KEY"] =""
os.environ["QIANFAN_SECRET_KEY"] =""

t2i=qianfan.Text2Image()
resp=t2i.do(
    prompt="A Ragdoll cat with a bowtie",
    with_decode="base64",
    model="Stable-Diffusion-XL",
)
img_data=resp["body"]["data"][0]["image"]

img=Image.open(io.BytesIO(img_data))
img.show()