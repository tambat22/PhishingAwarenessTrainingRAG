# Interactive Phishing Awareness Training


# 🛡️ AI Chatbot for Phishing Awareness Training

This project presents an interactive AI-powered chatbot that simulates realistic phishing scenarios to help users identify and avoid social engineering attacks. Built using the **Gemini API** and hosted locally via **Open WebUI** with bundled **Ollama** support, this tool engages users in phishing detection training using real-world datasets.

---

## 📽️ Demo

- 🎥 [Watch the YouTube demo](https://www.youtube.com/watch?v=X90PkgHIN9M)

---

## 🚀 Features

- Powered by **Gemini API** (Google's LLM)
- Hosted **locally** using **Open WebUI** and **Ollama**
- Uses **real phishing email datasets**
- Personalized, interactive phishing detection training
- Tracks user score and learning history
- Allows follow-up questions and clarifications
- Scalable and cost-effective for enterprise deployment

---

## 🛠️ Environment Setup

This chatbot runs locally using Docker and combines Open WebUI with Ollama for model interaction.

### 1️⃣ Install Docker

Download Docker:  
🔗 https://www.docker.com/products/docker-desktop

Ensure Docker is running before proceeding.

### 2️⃣ Launch Open WebUI + Ollama

Choose the command based on your hardware:

#### ✅ GPU-Supported Setup

```bash
docker run -d -p 3000:8080 --gpus=all \
  -v ollama:/root/.ollama \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:ollama
  ```

## 📊 Dataset Setup

The chatbot uses two phishing datasets to generate realistic training examples.

### 📁 Data Sources

Download and place the following datasets into your project:

- **Dataset 1** – [Phishing Email Dataset](https://www.kaggle.com/datasets/subhajournal/phishingemails)
- **Dataset 2** – [Phishing Emails](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)

Place them into the `data/` directory.
Run *data.py* to process and chunk the data into small parts suitable for LLM input.

---

## 🧹 Data Preprocessing

To ensure that the dataset is manageable by the chatbot and doesn't exceed the LLM context limit, large datasets are split into 5MB chunks.

## 💬 Chatbot Usage

1. Open the web interface at [http://localhost:3000](http://localhost:3000).
2. Select your model (e.g., **Gemini** via **Ollama** integration).
3. Paste the training prompt from `prompt.txt`.
📝 Example Prompt (prompt.txt)

```bash
You are a phishing awareness training assistant. I will type "START" to begin a 10-question quiz. For each question, give me a short message formatted as either a legitimate message or a phishing attempt, using a realistic format such as Outlook, Gmail, Slack, or Teams. Make the messages unique and contextually realistic. After each message, ask me to decide: "Phishing or Legitimate?"

Wait for my response before proceeding to the next question. Track my score silently. If I ask “why?” or request another example, explain clearly using features such as sender domain, urgency, or suspicious links. At the end of the 10 questions, tell me my total score and whether I passed the 80% threshold.
```
4. Type `START` to begin the session.
5. Review each message and reply with either: Legitimate or Phishing
6. Ask follow-up questions like:
- “Why is this suspicious?”
- “Can I see a similar example?”

7. After 10 questions, you’ll receive your **score** and a **pass/fail** result based on 80% accuracy.

---

## 📈 Chatbot Capabilities

- ⚠️ Simulates sophisticated phishing emails and normal messages
- 🧠 Understands user queries and adapts explanation detail
- 📝 Tracks all 10 answers and calculates score
- 🧪 Uses real dataset structure for realism
- 🧾 Works offline, customizable, and extendable

---

## 🔐 Security Considerations

- 💻 Runs completely **offline** on your machine
- 🔒 No data leaves your environment
- 🔍 Future plans to address:
  - LLM hallucination control
  - Prompt injection risks
  - Unauthorized prompt manipulation

---