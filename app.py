from openai import OpenAI

API_KEY = ""
BASE_URL = ""

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant",
        },
        {
            "role": "user",
            "content": "Hi",
        },
    ],
    stream=False,
)

print(response.choices[0].message.content)
