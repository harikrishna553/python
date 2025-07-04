# Step 1: Set user agent
import os
os.environ['USER_AGENT'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

# Step 2: Import the WebBaseLoader from LangChain community
from langchain_community.document_loaders import WebBaseLoader

# Step 3: Define the web path (URL)
url = "https://self-learning-java-tutorial.blogspot.com/"

# Step 4: Initialize the WebBaseLoader with the URL
loader = WebBaseLoader(web_paths=[url])

# Step 5: Load the web content
docs = loader.load()

# Step 6: Print the first page content
print(f"Total pages loaded: {len(docs)}")
print(f"Type of docs[0]: {type(docs[0])}")
print(f"First page content:\n{docs[0].page_content[:100]}")  # First 100 chars
print(f"Metadata:\n{docs[0].metadata}")