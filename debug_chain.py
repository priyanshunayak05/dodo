from llm_chain import stream_llm
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyApF3_yU0s-bzfL5Hv2O6Qk368wgH3cxI4"

print("Testing stream_llm...")
try:
    for chunk in stream_llm("Hello", provider="gemini"):
        print(chunk, end="", flush=True)
    print("\nDone.")
except Exception as e:
    print(f"\nError: {e}")
