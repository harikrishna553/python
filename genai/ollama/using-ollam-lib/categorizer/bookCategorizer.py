import ollama
import os

# Function to check if the input file exists, if not, it exits the program.
def check_input_file(file_path):
    """
    Check if the input file exists at the given path. If not, print an error and exit the program.
    """
    if not os.path.exists(file_path):
        print(f"Input File '{file_path}' not found")
        exit(1)

# Function to read book list from the file
def read_book_list(file_path):
    """
    Reads the book list from the specified file and returns it as a string.
    """
    with open(file_path, "r") as file:
        return file.read().strip()

# Function to create the prompt for the Ollama AI model
def create_prompt(book_list):
    """
    Creates the prompt to categorize and sort the books based on the given list.
    """
    return f"""
    You are an assistant that categorizes and sorts the books

    Here is the list of books

    {book_list}

    Please:
    1. Categorize these books into appropriate genres such as Fantasy, Literary, Thriller, Science Fiction, etc.
    2. Sort the books Alphabetically within each Genre.
    3. Present the categorized list in a clear and organized manner, using bullet points and numbering.
    """

# Function to call the Ollama model and generate categorized book list
def categorize_books(model, prompt):
    """
    Sends the prompt to the Ollama API and returns the categorized and sorted book list.
    """
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response.get("response", "")
    except Exception as e:
        print("An error occurred while generating the response:", str(e))
        return ""

# Function to write the categorized book list to an output file
def write_output(file_path, content):
    """
    Writes the given content to the specified output file.
    """
    with open(file_path, "w") as file:
        file.write(content.strip())

def main():
    """
    Main function to execute the categorization process.
    """
    # Print the current working directory for debugging purposes
    print("Current Working Directory:", os.getcwd())

    # Set the model and file paths
    model = "llama3.2"
    inputFile = "./data/bookList.txt"
    outputFile = "./data/bookListByCategory.txt"

    # Step 1: Check if the input file exists
    check_input_file(inputFile)

    # Step 2: Read the book list from the input file
    book_list = read_book_list(inputFile)

    # Step 3: Create the prompt to categorize books
    prompt = create_prompt(book_list)

    # Step 4: Categorize the books using the Ollama model
    categorized_books = categorize_books(model, prompt)

    if categorized_books:
        # Step 5: Write the categorized books to the output file
        write_output(outputFile, categorized_books)
        print(f"Categorized books are saved to '{outputFile}'")
    else:
        print("Failed to categorize books. Please check the error messages.")

if __name__ == "__main__":
    main()
