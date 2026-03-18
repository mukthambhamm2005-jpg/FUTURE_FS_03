🌱 Natural Forming RAG Chatbot

An intelligent Retrieval-Augmented Generation (RAG) chatbot built using Streamlit, ChromaDB, and Cohere, designed to provide practical guidance on natural forming techniques from uploaded PDF documents.

🚀 Features
📁 Upload multiple PDF documents
🔍 Extract and store document content using vector embeddings
🤖 Ask questions and get context-aware answers
🌿 Specialized responses focused on natural forming concepts
📚 View relevant document sources for each answer

🕒 Chat history tracking
🧠 Semantic search using embeddings

🛠️ Tech Stack
Frontend: Streamlit
Backend: Python
Vector Database: ChromaDB
LLM & Embeddings: Cohere API
PDF Processing: PyPDF2

🧠 How It Works
User uploads PDF documents
Text is extracted using PyPDF2
Cohere generates embeddings for the text
Data is stored in ChromaDB
User asks a question
Relevant documents are retrieved using similarity search
Cohere generates a contextual answer

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install dependencies
pip install -r requirements.txt
3. Add your Cohere API Key
Replace in code:
API_KEY = "your_api_key_here"
👉 Recommended: Use Streamlit secrets for security.
4. Run the app
streamlit run app.py
💡 Usage

Upload one or more PDF files from the sidebar
Click Upload All PDFs to Vector DB
Ask questions related to natural forming
View answers along with source documents

🌍 Example Questions
What are the principles of natural forming?
How can natural forming be applied in real-world scenarios?
What techniques are used in natural forming processes?

🔐 Note
The API key is hardcoded for demo purposes
For production, use environment variables or Streamlit secrets

🚀 Future Improvements
🌐 Deploy on cloud (Streamlit Cloud / AWS)
📊 Add document analytics
🧾 Support more file formats (DOCX, TXT)
🗣️ Voice input support
📱 Improve UI/UX

👨‍💻 Author
Mukthambha M M

GitHub: https://github.com/mukthambhamm2005-jpg
LinkedIn: https://www.linkedin.com/in/mukthambha-m-m-24b7082a5

⭐ Show Your Support
If you like this project, give it a ⭐ on GitHub!
