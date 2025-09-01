from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

system_prompt = """
Eres un científico preparado para hablar con niños de sexto grado.
Responde preguntas sobre ciencias en un lenguaje accesible para niños de sexto grado
Siempre que la pregunta no sea relacionada con la ciencia, responda que no sabes la respuesta
"""

llm = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages(
    messages=[
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{input}")
    ]
)

chain = prompt | llm | StrOutputParser()

print("Hola, soy profesor Spark, ¿en qué puedo ayudarte hoy?")

history = []

while True:    
    user_input = input("Tú: ")
    if user_input == "exit":
        break
          
    response = chain.invoke({"input": user_input, "history": history})
    print(f"Albert: {response}")

    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response))

print("¡Adiós!")