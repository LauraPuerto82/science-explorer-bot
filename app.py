import os
from dotenv import load_dotenv
import gradio as gr 

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import GoogleGenerativeAI

# ---------- Setup ----------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

with open("prompts/system.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

llm = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.5,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{input}"),
    ]
)
chain = prompt | llm | StrOutputParser()

def _history_to_langchain(history):
    lc = []
    for item in (history or []):
        role = item.get("role") 
        content = item.get("content", "")
        if role == "user": 
            lc.append(HumanMessage(content))
        elif role == "assistant": 
            lc.append(AIMessage(content))
    return lc

def generate_response(user_input, history):
    lc_history = _history_to_langchain(history)    
    try:
        resp = chain.invoke({"input": user_input, "history": lc_history})        
    except Exception:
        resp = "Oops! Something went wrong. Please try again. 🌟"
    return "", history + [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": resp},
    ]

def clear_chat():
    return "", []

# ---------- UI ----------
with open("assets/styles.css", "r", encoding="utf-8") as css_file:
    custom_css = css_file.read()

page = gr.Blocks(
    title="🌍 Science Explorer Chat - Professor Spark 🧑‍🏫",
    theme=gr.themes.Soft(), # type: ignore
    css=custom_css,
)

with page:
    # Header
    gr.HTML("""
        <div class="purple-card">
            <h1>🌍 Professor Spark's Science Lab 🧑‍🏫</h1>
            <p class="main-sub">Explore the universe with your favorite science teacher! ✨</p>
        </div>
    """)

    with gr.Row(elem_classes=["main-content"]):
        # LEFT column – all blocks as .purple-card (minimal & consistent)
        with gr.Column(elem_classes=["left-sidebar", "left-col"]):
            gr.HTML("""
                <div class="purple-card">
                    <h3>💬 Chat with Professor Spark!</h3>
                    <p><strong>How to chat:</strong> Type your question in the box and press <em>Enter</em>.</p>
                    <div class="chips-grid" style="margin-top:8px">
                        <span class="chip">🦖 How did a T-Rex live?</span>
                        <span class="chip">🕳️ What is a black hole?</span>
                        <span class="chip">🧪 Safe volcano experiment</span>
                        <span class="chip">🪐 Quiz me about planets</span>
                        <span class="chip">🚀 How does a rocket work?</span>
                    </div>
                </div>
            """)
            gr.HTML("""
                <div class="purple-card">
                    <h3>🌟 Fun Facts</h3>
                    <p>🫀 Octopuses have three hearts.</p>
                    <p>🪐 Jupiter could hold 1,300 Earths.</p>
                    <p>🦴 Brachiosaurus was over 20m tall.</p>
                </div>
            """)
            gr.HTML("""
                <div class="purple-card">
                    <h3>🌟 Thanks for exploring with Professor Spark!</h3>
                    <p>Stay curious and never stop asking questions! 🚀✨</p>
                </div>
            """)

        # RIGHT column – chat
        with gr.Column(elem_classes=["chat-container", "right-col"]):
            chatbot = gr.Chatbot(
                type="messages",
                avatar_images=(None, "assets/avatar.png"), 
                show_label=False,
                render_markdown=False,
                elem_classes=["chatbot"],
            )
            with gr.Row(elem_classes=["input-row"]):
                msg = gr.Textbox(
                    show_label=False,
                    placeholder="Ask me about dinosaurs, space, animals, or any science topic! 🦕🚀🦁🔬",
                    lines=1,
                    elem_classes=["textbox"],
                )
                clear = gr.Button("🧹 Clear", variant="secondary", elem_classes=["clear-btn"])

            msg.submit(fn=generate_response, inputs=[msg, chatbot], outputs=[msg, chatbot])
            clear.click(clear_chat, outputs=[msg, chatbot])

if __name__ == "__main__":
    page.launch()
