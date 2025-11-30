from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
import os
import requests
import json
import re

load_dotenv()

def get_llm(provider="gemini"):
    # This function is kept for compatibility if needed, but stream_llm handles gemini directly now
    if provider == "local":
        return OllamaLLM(model="llama3.2:1b")
    elif provider == "gemini":
        pass
    else:
        raise ValueError("Unsupported provider: choose 'gemini' or 'local'.")

def run_llm(prompt: str, provider="gemini"):
    if provider == "gemini":
        api_key = os.environ.get("GOOGLE_API_KEY")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        else:
            return f"Error: {response.text}"
    
    template = PromptTemplate.from_template("Answer the following:\n{question}")
    llm = get_llm(provider)
    chain = template | llm
    return chain.invoke({"question": prompt})

def stream_llm(prompt: str, provider="gemini"):
    if provider == "gemini":
        api_key = os.environ.get("GOOGLE_API_KEY")
        # Use streamGenerateContent for streaming
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:streamGenerateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}
        
        # Streaming request
        with requests.post(url, headers=headers, json=data, stream=True) as response:
            if response.status_code != 200:
                yield f"Error: {response.text}"
                return
            
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    # Regex to extract text content from the JSON lines
                    match = re.search(r'"text":\s*"(.*)"', decoded_line)
                    if match:
                        text = match.group(1)
                        # Handle escaped characters if necessary (basic unescape)
                        text = text.replace('\\n', '\n').replace('\\"', '"')
                        yield text
        return

    template = PromptTemplate.from_template("Answer the following:\n{question}")
    llm = get_llm(provider)
    chain = template | llm
    for chunk in chain.stream({"question": prompt}):
        yield chunk