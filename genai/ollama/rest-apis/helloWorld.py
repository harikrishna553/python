import requests
import json

# Define the API endpoint and payload
url = "http://localhost:11434/api/generate"
payload = {
    "model": "llama3.2",
    "prompt": "Tell me a joke",
    "stream": False
}

# Send the POST request to the Ollama API
response = requests.post(url, json=payload)

# Decode the response and parse JSON
if response.status_code == 200:
    decoded_response = response.content.decode('utf-8')
    json_response = json.loads(decoded_response)
    
    # Extract and print the LLM's response
    if "response" in json_response:
        print("Generated Response from Ollama LLM:")
        print(json_response["response"])
    else:
        print("No 'response' field found in the JSON.")
else:
    print(f"Error: {response.status_code}, Message: {response.text}")
