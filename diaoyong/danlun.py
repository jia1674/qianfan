import qianfan
import os

os.environ["QIANFAN_ACCESS_KEY"] =""
os.environ["QIANFAN_SECRET_KEY"] =""

chat_cump=qianfan.ChatCompletion()

resp=chat_cump.do(
    model="ERNIE-Bot",
    messages =[
        {
            "role": "user",
            "content": "你好"
        }
    ]
)

print(resp.body)