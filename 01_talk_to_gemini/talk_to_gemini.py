# Please make sure to install the required packages before running this code:
# pip install -r requirements.txt in windows or pip3 install -r requirements.txt on Mac

import google.genai as genai # Import the Google Generative AI library
from dotenv import load_dotenv # Import load_dotenv to manage environment variables

# Please make sure to set your Gemini API KEY in a .env file in the same folder, for this code to work.
# You can copy the .env_sample file and rename it to .env, then add your API key there.

def main(): # Main function to interact with Gemini model

    load_dotenv() # Load environment variables, which has the Gemini API KEY from .env file
    client = genai.Client() # Initialize the Gemini client

    while True: # Infinite loop to prompt the user for tne next question. Python does not have do-while loops.
        user_input = input("Say something to Gemini (or 'quit' to exit): ") # Get user input
        if user_input.lower() != "quit": # Check if the user does not want to quit
            try:
                # Next, calling the Gemini model to generate a response
                response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=user_input
                )
                
                print(f"✅ Gemini said: {response.text}") # Print the response from Gemini. Green tick mark is just to indicate success
            except Exception as e: # Catch any exceptions that occur during the API call
                print(f"❌ An error occurred: {e}") # Print the error message. Red cross mark is just to indicate failure
        else: # User has entered 'quit' to exit the conversation
            print("Exiting the conversation. Goodbye!") 
            break # Break the infinite loop to exit the conversation



if __name__ == "__main__": # Run the main function if this script is executed. This is boilerplate code.
    main()