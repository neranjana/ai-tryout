import google.genai as genai # Import the Google Generative AI library
from dotenv import load_dotenv # Import load_dotenv to manage environment variables



def main(): # Main function to interact with Gemini model

    load_dotenv() # Load environment variables, which has the Gemini API KEY from .env file
    client = genai.Client() # Initialize the Gemini client

    while True: 
        user_input = input("Say something to Gemini (or 'quit' to exit): ") # Get user input
        if user_input.lower() != "quit": #
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=user_input
                ) # Call the Gemini model to generate a response
                
                print(f"✅ Gemini said: {response.text}") # Print the response from Gemini
            except Exception as e: # Catch any exceptions that occur during the API call
                print(f"❌ An error occurred: {e}") # Print the error message
        else:
            print("Exiting the conversation. Goodbye!") # Exit the conversation
            break



if __name__ == "__main__": # Run the main function if this script is executed. This is boilerplate code.
    main()