# 🌍 World Explorer Bot - Profesor Spark

An educational chatbot designed for 6th-grade children that allows them to explore the world of science, dinosaurs, space, animals, and much more through interactive conversations.

## 🚀 Features

- **Educational chat in Spanish**: Specifically designed for 6th-grade children
- **Scientific topics**: Dinosaurs, space, animals, natural sciences
- **Adapted language**: Responses in accessible and understandable language for children
- **CLI interface**: Easy to use from the command line
- **Conversation history**: Maintains conversation context
- **Advanced AI**: Uses Google Gemini 2.0 Flash for intelligent responses

## 🎯 Objective

Create an educational tool that inspires scientific curiosity in children, allowing them to ask questions about topics that interest them and receive clear and educational answers.

## 🛠️ Technologies Used

- **Python 3.x**
- **LangChain**: Framework for AI applications
- **Google Gemini 2.0 Flash**: Advanced language model
- **Gradio**: For future web interfaces (in development)

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

2. **Interact with Profesor Spark:**
   - Type your questions about science, dinosaurs, space, animals, etc.
   - The bot will respond in an educational and understandable way
   - Type `exit` to quit

## 🔧 Configuration

### Getting Google AI Studio API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create an account or sign in
3. Generate a new API key
4. Copy the key to your `.env` file

## 📚 Usage Examples

```
You: ¿Por qué los dinosaurios se extinguieron?
Profesor Spark: ¡Excelente pregunta! Los dinosaurios se extinguieron hace unos 65 millones de años, probablemente debido a un asteroide gigante que golpeó la Tierra...

You: ¿Cómo se forman las estrellas?
Profesor Spark: Las estrellas se forman en nubes gigantes de gas y polvo llamadas nebulosas...
```

## 🚧 Upcoming Improvements

- [ ] **Gradio Interface**: Child-friendly web interface
- [ ] **Multi-language Support**: Spanish and English
- [ ] **Child-friendly Interface**: Colorful and attractive design for children
- [ ] **Offline Mode**: Predefined responses for offline use
- [ ] **Achievement System**: Gamification to motivate learning
- [ ] **Customizable Topics**: Different scientific categories

## 🤝 Contributions

This is an educational project in development. Contributions are welcome, especially:
- User interface improvements
- New scientific topics
- Performance optimizations
- Translations and localization

## 📝 License

This project will be under the MIT license. (License file coming soon!)

## 👨‍🏫 About the Project

Developed to create an educational tool that makes science accessible and fun for children. The bot is designed to answer questions clearly and understandably, fostering scientific curiosity and love for learning.
---

**Enjoy exploring the world with Profesor Spark! 🌟**
