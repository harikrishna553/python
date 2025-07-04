from langchain_text_splitters import HTMLHeaderTextSplitter

# Define the HTML string to split
html_string = """
<!DOCTYPE html>
<html>
  <head>
    <title>Introduction to Machine Learning</title>
  </head>
  <body>
    <h1>Machine Learning Overview</h1>
    <p>Machine Learning is a subfield of artificial intelligence that focuses on building systems that learn from data.</p>
    
    <h2>Types of Machine Learning</h2>
    <p>There are mainly three types: supervised learning, unsupervised learning, and reinforcement learning.</p>
    
    <h3>Supervised Learning</h3>
    <p>In supervised learning, the model is trained on a labeled dataset. Common algorithms include Linear Regression, Decision Trees, and Support Vector Machines.</p>
    
    <h3>Unsupervised Learning</h3>
    <p>Unsupervised learning uses data without labels. Clustering and dimensionality reduction are common tasks in this category.</p>
    
    <h3>Reinforcement Learning</h3>
    <p>Reinforcement learning is based on rewarding desirable behaviors and/or punishing undesirable ones. It is often used in robotics and gaming.</p>
    
    <h2>Applications of Machine Learning</h2>
    <p>Machine learning is widely used in image recognition, natural language processing, recommendation systems, fraud detection, and more.</p>
    
    <h2>Challenges in Machine Learning</h2>
    <p>Some of the key challenges include data quality, model interpretability, overfitting, and computational costs.</p>
  </body>
</html>
"""

# Define the headers to split on
headers_to_split_on = [
    ("h1", "Header One"),
    ("h2", "Header Two"),
    ("h3", "Header Three"),
]

# Create the HTMLHeaderTextSplitter with specified headers
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

# Perform the splitting
html_header_splits = html_splitter.split_text(html_string)

# Display the results
for i, doc in enumerate(html_header_splits, start=1):
    print(f"--- Chunk {i} ---")
    print("Content:")
    print(doc.page_content)
    print("Metadata:")
    print(doc.metadata)
    print("----------------\n")
