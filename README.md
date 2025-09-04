# 🌍 World Explorer Bot - Professor Spark

An educational chatbot designed for children that allows them to explore the world of science, dinosaurs, space, animals, and much more through interactive conversations.

## 🚀 Features

- **Educational chat**: Specifically designed for children with age-appropriate language
- **Scientific topics**: Dinosaurs, space, animals, natural sciences
- **Web interface**: Beautiful, responsive Gradio interface with mobile support
- **Children-friendly design**: Purple gradient theme with Professor Spark character
- **Multi-language support**: Responds in the same language as the user
- **Conversation history**: Maintains conversation context
- **Advanced AI**: Uses Google Gemini 2.0 Flash for intelligent responses

## 🎯 Objective

Create an educational tool that inspires scientific curiosity in children, allowing them to ask questions about topics that interest them and receive clear and educational answers.

## 🛠️ Technologies Used

- **Python 3.x**
- **LangChain**: Framework for AI applications
- **Google Gemini 2.0 Flash**: Advanced language model
- **Gradio**: Web interface framework
- **CSS**: Responsive design with mobile-first approach

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI Studio account with API key
- Internet connection

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd world-explorer-bot-project
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables:**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## 🎮 Usage

1. **Run the application:**

   ```bash
   python app.py
   ```

2. **Open your browser** and go to the local URL shown in the terminal (usually `http://127.0.0.1:7860`)

3. **Interact with Professor Spark:**
   - Type your questions about science, dinosaurs, space, animals, etc.
   - The bot will respond in an educational and understandable way
   - Use the "Clear" button to start a new conversation

## 🔧 Configuration

### Getting Google AI Studio API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create an account or sign in
3. Generate a new API key
4. Copy the key to your `.env` file

## 📚 Usage Examples

```
You: Why did dinosaurs go extinct?
Professor Spark: Great question! Dinosaurs went extinct about 65 million years ago, probably due to a giant asteroid that hit Earth...

You: How do stars form?
Professor Spark: Stars form in giant clouds of gas and dust called nebulae...
```

## 📝 License

This project will be under the MIT license. (License file coming soon!)

## 👨‍🏫 About the Project

Developed to create an educational tool that makes science accessible and fun for children. The bot is designed to answer questions clearly and understandably, fostering scientific curiosity and love for learning.

---

**Enjoy exploring the world with Professor Spark! 🌟**
