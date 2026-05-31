<div align="center">
  <img src="frontend/logo.jpg" alt="CodeLens Logo" width="120"/>
  <h1>CodeLens ⚡</h1>
  <p><strong>AI-Powered Code Complexity & Optimization Analyzer</strong></p>
  
  <a href="https://trycodelens.vercel.app/"><strong>Explore the Live Application »</strong></a>
  
  <br>
  <br>
  
  ![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
  ![Vanilla JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
  ![Gemini AI](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
</div>

<hr>

## ⌘ The Intelligence Engine

CodeLens is a decoupled, full-stack analytical tool designed to evaluate algorithmic efficiency in real-time. By leveraging large language models, it identifies inefficient patterns, calculates Big-O time and space complexity, and generates optimized code variants instantly.

## 🚀 Core Capabilities

- **Deep Algorithmic Analysis:** Real-time Big-O time and space complexity extraction.
- **Intelligent Refactoring:** Identifies redundant operations, nested loop traps, and memory leaks.
- **Multi-Language Support:** Native parsing for Python, JavaScript, Java, C++, TypeScript, Go, and Rust.
- **Optimized Output:** Side-by-side original vs. optimized code comparison with syntax highlighting.
- **Monorepo Architecture:** Cleanly separated static frontend (Vercel) and Python API (Render).

## 🏗️ System Architecture

- **Frontend:** Vanilla JS, HTML5, CSS3, Highlight.js
- **Backend:** Python, FastAPI, Uvicorn
- **AI Integration:** `google-generativeai` (Gemini Pro)

## ⚡ Local Deployment

Clone the repository and boot the intelligence engine locally:

```bash
# 1. Clone the repository
git clone [https://github.com/adithyachary09/CodeLens.git](https://github.com/adithyachary09/CodeLens.git)
cd CodeLens/backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables
# Create a .env file in the backend directory and add your API key:
GEMINI_API_KEY=your_google_gemini_api_key

# 4. Boot the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000