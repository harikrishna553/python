from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
LangChain is a framework for developing applications powered by large language models (LLMs).

LangChain simplifies every stage of the LLM application lifecycle:

Development: Build your applications using LangChain's open-source components and third-party integrations. Use LangGraph to build stateful agents with first-class streaming and human-in-the-loop support.
Productionization: Use LangSmith to inspect, monitor and evaluate your applications, so that you can continuously optimize and deploy with confidence.
Deployment: Turn your LangGraph applications into production-ready APIs and Assistants with LangGraph Platform.
"""

text_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)

# input is a list of raw strings
docs = text_splitter.create_documents([text])

print(f"Type Of Document : {type(docs[0])}")  # <class 'langchain_core.documents.base.Document'>
print(f"Total Documents : ' + {len(docs)}")
print(f"First Page Content: {docs[0].page_content}")
print(f"Second Page Content: {docs[1].page_content}")
