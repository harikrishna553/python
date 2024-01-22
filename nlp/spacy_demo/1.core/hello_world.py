import spacy

try:
    # Load a spaCy model to check if it's installed
    nlp = spacy.load("en_core_web_sm")
    # If you reach this point, spacy is installed
    print("spacy is installed successfully.")
    print("spacy version:", spacy.__version__)
except ImportError:
    print("spacy is not installed or not configured correctly.")
except Exception as e:
    print("An error occurred while checking spaCy installation:", e)
