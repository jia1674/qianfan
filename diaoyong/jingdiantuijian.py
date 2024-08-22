import qianfan
import os

# 设置环境变量
os.environ["QIANFAN_ACCESS_KEY"] = ""
os.environ["QIANFAN_SECRET_KEY"] = ""

def get_travel_recommendations(user_input):
    # 创建Completion对象
    comp = qianfan.Completion()
    # 调用API获取推荐
    response = comp.do(
        method="EBNIE-Bot-4",  # 假设这是API的正确方法名
        prompt=f"根据以下用户偏好推荐旅游景点:\n{user_input}\n推荐理由:",
        temperature=0.7,
        top_p=1
    )
    # 从响应中提取推荐结果
    recommendations = response.body["result"]  # 假设response.body是正确的方法来获取结果
    return recommendations

# 假设user_input是一个字符串变量，包含用户的偏好
user_input = ("""
偏好：历史遗迹和文化体验
旅行时间：2023年4月
预算：中等
""")
recommendations = get_travel_recommendations(user_input)
print(recommendations)