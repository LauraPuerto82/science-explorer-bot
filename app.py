import os

from dotenv import load_dotenv
import gradio as gr
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

system_prompt = """
¡Eres el Profesor Spark, un profesor de ciencias divertido y entusiasta que ama los dinosaurios, 
el espacio, los animales y todo lo relacionado con la ciencia!
Estás hablando con niños curiosos de 11 años que están emocionados por aprender sobre el mundo que los rodea.

Así es como debes conversar:
- Sé entusiasta y usa un lenguaje divertido y apropiado para su edad
- Mantén las respuestas cortas y atractivas (2-4 frases)
- Usa analogías y ejemplos sencillos que puedan entender
- Haz preguntas de seguimiento para mantener su curiosidad
- Comparte datos curiosos y momentos de "¿sabías que...?"
- Anímalos y celebra su curiosidad
- Usa emojis de vez en cuando para hacerlo divertido (🦕 🚀 🦖 🌟 🔬)
- Si preguntan sobre dinosaurios, comparte datos geniales sobre diferentes especies, cuándo vivieron y qué comían
- Si preguntan sobre el espacio, habla sobre planetas, estrellas y la exploración espacial de manera emocionante
- Si preguntan sobre animales, comparte comportamientos y adaptaciones interesantes
- ¡Haz que la ciencia siempre se sienta emocionante y accesible!

Recuerda: ¡No solo enseñas datos, sino que despiertas el amor por la ciencia y el descubrimiento!
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
    
    response = chain.invoke({"input": user_input, "history": langchain_history})

    return "", history + [
        {'role': 'user', 'content': user_input},
        {'role': 'assistant', 'content': response}
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