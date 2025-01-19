import ollama
from datetime import datetime

# Fetch the list of available LLMs
llms_in_my_system = ollama.list()

# Print the output in a table format
print(f"{'Model Name':<10} {'Modified At':<15} {'Digest':<20} {'Size (bytes)':<5} {'Parameter Size':<15} {'Quantization Level':<10}")
print("-" * 140)

for model in llms_in_my_system.models:
    model_name = model.model
    modified_at = model.modified_at.strftime("%Y-%m-%d %H:%M:%S")  # Format datetime
    digest = model.digest
    size = model.size
    parameter_size = model.details.parameter_size
    quantization_level = model.details.quantization_level

    print(f"{model_name:<20} {modified_at:<25} {digest:<40} {size:<15} {parameter_size:<15} {quantization_level:<20}")
