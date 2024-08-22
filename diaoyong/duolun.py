import qianfan
import os

os.environ["QIANFAN_ACCESS_KEY"] =""
os.environ["QIANFAN_SECRET_KEY"] =""

chat_cump=qianfan.ChatCompletion()

resp=chat_cump.do(
    messages =[
        {
            "role": "user",
            "content": "你好"
        },
        {
            "role": "assistant",
            "content": "你好！很高兴与你交流。请问你有什么需要我帮助解答的问题吗？"
        },
        {
            "role": "user",
            "content": "我在做一个基于大数据的应用，需要找到一个合适的机器学习算法。"
        }
    ]
)

print(resp.body)