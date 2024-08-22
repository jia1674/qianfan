import qianfan
import os

os.environ["QIANFAN_ACCESS_KEY"] =""
os.environ["QIANFAN_SECRET_KEY"] =""

cump=qianfan.Completion()

resp=cump.do(model="ERNIE-Bot",prompt="你好",stream=True)

for line in resp:
    print(line)