# Please make sure to install the required packages before running this code:
# pip install -r requirements.txt in windows or pip3 install -r requirements.txt on Mac

import os # Import os module to access environment variables
from openai import OpenAI # Import the OpenAI library
from dotenv import load_dotenv # Import load_dotenv to manage environment variables

# Please make sure to set your OpenAI API KEY in a .env file in the same folder, for this code to work.
# You can copy the .env_sample file and rename it to .env, then add your API key there.

def main(): # Main function to interact with ChatGPT model

    load_dotenv() # Load environment variables, which has the OpenAI API KEY from .env file
    api_key = os.getenv("OPENAI_API_KEY") # Get OpenAI API key from environment variable
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set it by including it in the .env file or exporting it in your shell.")
        return
    client = OpenAI(api_key=api_key) # Initialize the OpenAI client

    while True: # Infinite loop to prompt the user for tne next question. Python does not have do-while loops.
        user_input = input("Say something to ChatGPT (or 'quit' to exit): ") # Get user input
        if user_input.lower() != "quit": # Check if the user does not want to quit
            print("Calling ChatGPT API... please wait.") # Inform the user that the API call is in progress
            try:
                # Next, calling the OpenAI model to generate a response
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": user_input}
                    ]
                )
                
                print(f"✅ ChatGPT said: {response.choices[0].message.content}") # Print the response from ChatGPT. Green tick mark is just to indicate success
            except Exception as e: # Catch any exceptions that occur during the API call
                print(f"❌ An error occurred: {e}") # Print the error message. Red cross mark is just to indicate failure
        else: # User has entered 'quit' to exit the conversation
            print("Exiting the conversation. Goodbye!") 
            break # Break the infinite loop to exit the conversation



if __name__ == "__main__": # Run the main function if this script is executed. This is boilerplate code.
    main()