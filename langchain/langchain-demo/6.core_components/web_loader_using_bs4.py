# Step 1: Set user agent (to avoid blocking by the site)
import os
os.environ['USER_AGENT'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

# Step 2: Import required modules
from langchain_community.document_loaders import WebBaseLoader
from bs4 import SoupStrainer

# Step 3: Define the URL to load
url = "https://self-learning-java-tutorial.blogspot.com/"

# Step 4: Define which HTML elements to extract using SoupStrainer
strainer = SoupStrainer(class_=["hariGroupHeader", "hariGroupContent"])

# Step 5: Initialize the WebBaseLoader with bs4 filtering
loader = WebBaseLoader(
    web_paths=[url],
    bs_kwargs={"parse_only": strainer}
)

# Step 6: Load the filtered web content
docs = loader.load()

# Step 7: Inspect the result
print(f"Total pages loaded: {len(docs)}")
print(f"Type of docs[0]: {type(docs[0])}")
print("---- Extracted Content ----")
print(docs[0].page_content[:500])  # This will contain only the filtered content
print("---- Metadata ----")
print(docs[0].metadata)
