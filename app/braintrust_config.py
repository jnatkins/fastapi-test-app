import os
from braintrust import init

def initialize_braintrust():
    """
    Initialize the Braintrust SDK with your credentials.
    
    Set your Braintrust API key as an environment variable named BRAINTRUST_API_KEY
    or directly here (not recommended for production).
    """
    api_key = os.environ.get("BRAINTRUST_API_KEY")
    
    if not api_key:
        print("Warning: BRAINTRUST_API_KEY environment variable not set.")
        print("Tracing data will not be sent to Braintrust.")
        print("Set this variable or configure the API key in the code for production use.")
        return
    
    # Initialize Braintrust with your API key and project
    #init(
    #    api_key=api_key,
    #    project="Issue Repros",
        # Optional: Set the environment
        # environment="development"
    #)
    
    print("Braintrust SDK initialized successfully!") 