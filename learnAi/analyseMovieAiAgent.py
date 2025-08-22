import os

from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI


def chatwithOpenAi(inputMsg):
    api_key = "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"
    # prompting
    inputPrompt = ChatPromptTemplate.from_messages(
        [("system", "You are a helpful AI Assistant more effective for Movies created by Koushik. Your name is Jarvis"),
         ("human", "Enter your query {msg}")]
    )

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    response = client.chat.completions.create(model="tngtech/deepseek-r1t2-chimera:free", messages=[{"role": "user",
                                                                                                     "content": inputMsg}])

    # Create chain
    aiOutput = response.choices[0].message.content.encode('ascii', 'ignore').decode('ascii')
    aiOutput = aiOutput.replace('\n\n', "", 1)
    return str(aiOutput)


def chatwithDf(inputMsg):
    apiKey = "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"
    import pandas as pd
    df = pd.read_csv(os.path.join("datasets", "Cars_Datasets_2025.csv"), encoding='latin1')
    # prompting
    inputPrompt = ChatPromptTemplate.from_messages(
        [("system", "You are a helpful AI Assistant more effective for Movies created by Koushik. Your name is Jarvis"),
         ("human", "Enter your query {msg}")]
    )

    # Create LLM
    llm = HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta")
    aiOutput = StrOutputParser()

    # Create chain
    chain = inputPrompt | llm | aiOutput
    response = chain.invoke({"msg": inputMsg})
    return response


if __name__ == "__main__":
    chat = True
    while chat:
        userInput = input("You : ")
        if userInput.lower() in ["goodbye", "bye", "quit", "exit"]:
            print("AI : Goodbye! Take care, and feel free to reach out if you need anything in the future.")
            chat = False
        else:
            response = chatwithOpenAi(userInput)
            print("AI : " + str(response))
