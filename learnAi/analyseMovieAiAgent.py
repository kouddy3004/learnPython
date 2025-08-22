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

    # response = llm.chat.completions.create( messages=[{"role": "user","content": inputMsg}])
    # aiOutput = response.choices[0].message.content.encode('ascii', 'ignore').decode('ascii')
    # aiOutput = aiOutput.replace('\n\n', "", 1)

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
