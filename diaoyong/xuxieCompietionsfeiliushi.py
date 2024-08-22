import qianfan
import os

os.environ["QIANFAN_ACCESS_KEY"] =""
os.environ["QIANFAN_SECRET_KEY"] =""

cump=qianfan.Completion()

resp=cump.do(prompt="你好")

print(resp)