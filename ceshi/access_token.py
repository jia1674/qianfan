import json
import requests


def main():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    payload = {
        'client_id': '',  # 请替换为您的 client_id
        'client_secret': '',  # 请替换为您的 client_secret
        'grant_type': 'client_credentials'
    }

    # 发送表单数据
    response = requests.post(url, data=payload)

    # 打印状态码和响应内容
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    # 尝试解析 JSON 响应
    try:
        return response.json().get('access_token')
    except json.JSONDecodeError:
        print("Failed to decode JSON response")
        return None


if __name__ == "__main__":
    access_token = main()
    print(access_token)
