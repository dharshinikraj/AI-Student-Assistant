#  StudBud AI

StudBud AI is an AI-powered study companion built to make learning more interactive and less overwhelming.

Whether you're preparing for exams, learning a new topic, revising notes, or simply stuck on a concept, StudBud helps you learn through conversations, personalized study plans, quizzes, summaries, and PDF-based question answering.

The goal of this project was simple: create a single platform where students can study smarter using AI instead of switching between multiple tools.

---

## Features

### ● AI Chat Assistant

Ask questions just like you would ask a teacher or mentor. StudBud explains concepts in a simple and easy-to-understand way.

### ● Conversation Memory

The assistant remembers the context of the conversation, making interactions feel more natural and personalized.

### ● Quiz Generator

Generate quizzes on any topic to test your understanding and reinforce learning.

### ● Study Planner

Create structured study plans based on your learning goals and available time.

### ● Topic Summarizer

Get quick summaries of complex topics along with examples and practical applications.

### ● PDF Assistant

Upload your notes and ask questions directly from the document. StudBud combines information from the uploaded PDF with its general knowledge to provide helpful answers.

### ● Chat Export

Download your chat history and keep it for revision or future reference.

---

##  Built With

* Python
* Streamlit
* Groq API
* Llama 3.3 70B
* PyPDF
* Python Dotenv

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/studbud-ai.git
cd studbud-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file in the project folder:

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

---

##  Why I Built This

As a student, I often found myself using different tools for note reading, planning, revision, quizzes, and doubt-solving. I wanted to create a single AI-powered platform that could bring these study activities together and make learning more efficient.

StudBud AI was developed as a project to explore Large Language Models, conversational AI, prompt engineering, context management, and document-based question answering while building something genuinely useful for students.

---

##  What I Learned

While building this project, I gained hands-on experience with:

* Large Language Model integration
* Prompt engineering
* Conversational memory systems
* PDF text extraction
* Streamlit application development
* API integration with Groq
* Building AI-powered educational tools

---

##  Future Improvements

* Flashcard generation
* Multiple PDF support
* User authentication
* Progress tracking
* Personalized learning recommendations
* Voice-based interactions

---



