import spacy

def nlp_model(model_name='en_core_web_sm'):
    try:
        # Load a spaCy model to check if it's installed
        nlp = spacy.load(model_name)
        # If you reach this point, spacy is installed
        print(f'Model {model_name} is loaded successfully.')
        return nlp
    except ImportError:
        print("spacy is not installed or not configured correctly.")
    except Exception as e:
        print("An error occurred while checking spaCy installation:", e)