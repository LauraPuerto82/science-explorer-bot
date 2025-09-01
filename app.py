import os

from dotenv import load_dotenv
import gradio as gr
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

with open("prompts/system.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()

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

llm = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)

prompt = ChatPromptTemplate.from_messages(
    messages=[
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{input}")
    ]
)

chain = prompt | llm | StrOutputParser()

def generate_response(user_input, history):     
    langchain_history = []
    for item in history:
        if item['role'] == 'user':
            langchain_history.append(HumanMessage(item['content']))
        elif item['role'] == 'assistant':
            langchain_history.append(AIMessage(item['content']))
    
    try:
        response = chain.invoke({"input": user_input, "history": langchain_history})
        return "", history + [
            {'role': 'user', 'content': user_input},
            {'role': 'assistant', 'content': response}
        ]
    except Exception as e:
        error_msg = f"Lo siento, tuve un problema técnico. ¿Podrías intentar de nuevo? Error: {str(e)}"
        return "", history + [
            {'role': 'user', 'content': user_input},
            {'role': 'assistant', 'content': error_msg}
        ]
    
def clear_chat():
    return "", []

page = gr.Blocks(
    title="Science Explorer Chat",
    theme=gr.themes.Soft()    
)

with page:
    gr.Markdown(
        """
        # 🌍 Chat del Profesor Spark 🧑‍🏫
        
        **¡Bienvenido a tu aventura con el Profesor Spark!** 🌟
        
        Pregúntame sobre:
        - 🦖 **Dinosaurios** - ¡Aprende sobre el T-Rex, Triceratops y muchos más!
        - 🚀 **Espacio** - ¡Descubre planetas, estrellas y los misterios del universo!
        - 🦁 **Animales** - ¡Explora criaturas asombrosas y sus superpoderes!
        - 🔬 **Ciencia** - ¡Descubre los secretos de cómo funcionan las cosas!
        - 🌍 **La Tierra** - ¡Viaja por volcanes, océanos y mucho más!
        
        *¿Qué te gustaría explorar hoy?*
        """
    )
    
    chatbot = gr.Chatbot(
        type="messages", 
        avatar_images=[None, "assets/avatar.png"],
        show_label=False,    
    )
    
    msg = gr.Textbox(
        show_label=False, 
        placeholder="Pregúntame sobre dinosaurios, espacio, animales, o cualquier tema de ciencia! 🦕🚀",        
    )
        
    msg.submit(
        fn=generate_response, 
        inputs=[msg, chatbot], 
        outputs=[msg, chatbot]
    )
    
    clear = gr.Button("🧹 Limpiar Chat", variant="secondary")                  
    clear.click(clear_chat, outputs=[msg, chatbot])

page.launch()