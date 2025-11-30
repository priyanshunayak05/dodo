# How to Run the RAG Chatbot Locally (Gemini Edition)

This guide will help you run the RAG Chatbot project on your local machine using **Google Gemini**.

## Prerequisites

1.  **Python 3.10+**: Ensure Python is installed.
2.  **Google API Key**: You need a key from [Google AI Studio](https://aistudio.google.com/).
    *   *Note: The key is currently configured in your `.env` file.*

## Setup

1.  **Navigate to the project directory**:
    ```powershell
    cd path\to\rag_project
    ```

2.  **Install Dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```

## Running the Application

You need to run **two** separate terminals.

### Terminal 1: Backend Server (FastAPI)

Run the following command to start the backend API:

```powershell
# Set the API key if not in .env, otherwise just run python main.py
$env:GOOGLE_API_KEY='AIzaSyApF3_yU0s-bzfL5Hv2O6Qk368wgH3cxI4'; python main.py
```

*   You should see `Uvicorn running on http://127.0.0.1:8000`.
*   Keep this terminal open.

### Terminal 2: Frontend (Streamlit)

Open a **new** terminal window, navigate to the project folder, and run:

```powershell
streamlit run app.py
```

*   This will automatically open your browser to `http://localhost:8501`.
*   You can now upload files and chat with them!

## Troubleshooting

*   **Connection Refused**: Make sure the Backend Server (Terminal 1) is running before you try to upload files in the Frontend.
*   **API Key Errors**: Ensure `GOOGLE_API_KEY` is set correctly in your environment or `.env` file.
