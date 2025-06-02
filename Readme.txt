This Streamlit app summarizes content from YouTube videos and webpages using Langchain and Groq LLMs.

🔧 Features
✅ Summarize YouTube videos and website content

✅ Choose from multiple Groq models (e.g., llama3, gemma2, deepseek)

✅ Adjustable temperature for model creativity

✅ Simple UI with Streamlit

🚀 How to Use
Clone this repo and install dependencies.

Run the app:

bash
Copy
Edit
streamlit run app.py
Enter your Groq API key in the sidebar.

Paste a YouTube URL or any valid website link.

Click "Summarize" to get a 300-word summary.

📦 Requirements
Python 3.9+

streamlit

langchain

langchain_groq

langchain_community

validators

Install with:

bash
Copy
Edit
pip install streamlit langchain langchain_groq langchain_community validators
📌 Notes
Only public YouTube videos or accessible websites are supported.

Summary length is approximately 300 words.