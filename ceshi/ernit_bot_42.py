import json
import requests


def main():
    access_token = ''
    url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=' + access_token
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "请介绍你自己"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)  # 使用 requests.post 发送请求
    print(response.text)

if __name__ == "__main__":
    main()