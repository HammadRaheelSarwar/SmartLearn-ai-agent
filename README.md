# 🤖 SmartLearn AI Agent

SmartLearn AI Agent is an intelligent AI-powered learning assistant designed to help users interact with educational content through smart agents. The system provides intelligent responses, configurable workflows, and persistent memory to enhance the learning experience.

---

# 🚀 Features

* 🤖 AI-powered learning assistant
* 🧠 Memory-based conversation tracking
* ⚙️ Configurable AI agents using YAML configuration
* 🌐 Web interface for interacting with the AI system
* 📊 Modular Python architecture
* 💾 Persistent memory storage using JSON

---

# 🛠️ Technologies Used

* Python
* AI Agents Architecture
* YAML Configuration
* JSON Memory Storage
* Web Interface (Python)
* Environment Variables (.env)

---

# 📂 Project Structure

```
SmartLearn-ai-agent
│
├── agents.py          # AI agent logic
├── app.py             # Application controller
├── main.py            # Main program execution
├── web.py             # Web interface
├── config.yaml        # Agent configuration
├── memory.json        # AI memory storage
├── requirements.txt   # Python dependencies
├── .env               # Environment variables
└── README.md          # Project documentation
```

---

# ⚙️ Installation Guide

Follow these steps to set up the project locally.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/HammadRaheelSarwar/SmartLearn-ai-agent.git
```

---

## 2️⃣ Navigate to the Project Folder

```bash
cd SmartLearn-ai-agent
```

---

## 3️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Configure Environment Variables

Create a `.env` file in the root directory and add your API keys.

Example:

```
OPENAI_API_KEY=your_api_key_here
```

You can add additional configuration variables if required.

---

# ▶️ Running the Project

## Run Main AI Agent

```bash
python main.py
```

---

## Run Web Interface

```bash
python web.py
```

After running the web interface, open your browser and go to:

```
http://localhost:5000
```

*(Port may vary depending on configuration.)*

---

# 🧠 How It Works

1. User interacts with the AI agent
2. The agent processes input using configured logic
3. Memory is stored in `memory.json`
4. The AI responds with intelligent output

---

# 🔮 Future Improvements

* User authentication system
* AI learning progress dashboard
* Advanced AI agent workflows
* Integration with external learning APIs

---

# 👨‍💻 Author

**Hammad Raheel Sarwar**

GitHub
https://github.com/HammadRaheelSarwar

---

⭐ If you found this project useful, consider giving it a **star on GitHub**.
