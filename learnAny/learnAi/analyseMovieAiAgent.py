import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# From LLM
api_key = "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"
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    model="tngtech/deepseek-r1t2-chimera:free"
)
aiOutput = StrOutputParser()


def chatwithOpenAi(inputMsg):
    # prompting
    inputPrompt = ChatPromptTemplate.from_messages(
        [("system", "You are a helpful AI Assistant more effective for For my AI Learning created by Koushik. Your name is Koushik's Bot"),
         ("human", "Enter your query {msg}")]
    )

    # Create chain
    chain = inputPrompt | llm
    response = chain.invoke({"msg": inputMsg})
    aiOutput = response.content.encode('ascii', 'ignore').decode('ascii')
    aiOutput = aiOutput.replace('\n\n', "", 1)
    return str(aiOutput)


def chatWithPandas(userInput):
    # From CSV
    import pandas as pd
    df = pd.read_csv(os.path.join("datasets", "Cars_Datasets_2025.csv"), encoding='latin1')


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
