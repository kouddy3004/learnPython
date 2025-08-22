from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

completion = client.chat.completions.create(
    # model="openai/gpt-oss-20b:free",
    model="tngtech/deepseek-r1t2-chimera:free",
    messages=[
        {
            "role": "user",
            "content": "hi"
        }
    ]
)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(completion.choices[0].message.content)
