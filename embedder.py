"""
embedder.py

This module provides functions to convert text data into vector embeddings
using Google Gemini Embeddings. This is cloud-based and memory-efficient.

Functions:
    embed_texts(chunks): Embeds a list of text chunks into vectors.
    embed_query(text): Embeds a single query string into a vector.
"""
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

# Initialize Google Embeddings
# Note: This requires GOOGLE_API_KEY to be set in environment variables
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

import time
import random

def embed_texts(chunks):
    """
    Embed a list of text chunks into vector representations.
    Includes retry logic for rate limits.
    """
    batch_size = 10  # Process in smaller batches to avoid hitting limits
    all_embeddings = []
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i+batch_size]
        retries = 3
        for attempt in range(retries):
            try:
                batch_embeddings = embeddings.embed_documents(batch)
                all_embeddings.extend(batch_embeddings)
                break
            except Exception as e:
                if "429" in str(e) and attempt < retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    print(f"Rate limit hit. Retrying in {wait_time:.2f}s...")
                    time.sleep(wait_time)
                else:
                    raise e
        # Add a small delay between batches
        time.sleep(1) 
        
    return all_embeddings

def embed_query(text):
    """
    Embed a single query string into a vector representation.
    """
    retries = 3
    for attempt in range(retries):
        try:
            return embeddings.embed_query(text)
        except Exception as e:
            if "429" in str(e) and attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise e
