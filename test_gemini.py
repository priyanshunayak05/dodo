from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set the key directly for testing
os.environ["GOOGLE_API_KEY"] = "AIzaSyApF3_yU0s-bzfL5Hv2O6Qk368wgH3cxI4"

try:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    response = llm.invoke("Say hello")
    print("Success:", response.content)
except Exception as e:
    print("Error:", e)
