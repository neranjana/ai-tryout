# Talk to ChatGPT Simple Commandline Chat program

This program simply allows a user to ask questions from OpenAI ChatGPT.

## How to use

1. Preferably, create a venv (virtual Python environment) but it is not mandatory
2. Install dependencies by executing requirements.txt by executing the following command in this folder.<br/> `pip install -r requirements.txt` in windows or `pip3 install -r requirements.txt` on Mac
3. Copy `.env_sample` file as `.env` in the same directory. Modify the file and substitute the `xxxxxxxxxx` with the OpenAI API Key. You can get a key by following the instructions stated [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)
4. Run the `talk_to_chat_gpt.py` program on the command line. On windows `talk_to_chat_gpt.py` or on Mac `python3 talk_to_chat_gpt.py`
5. Enter any text, any question you want to ask ChatGPT on the command prompt and press enter. You will get the answer. 
6. The program will keep on prompting for the next question. Please enter `quit` and hit enter to exit the program