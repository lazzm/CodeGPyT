# CodeGPyT

CodeGPyT is a Python program that uses OpenAI code-davinci model to generate code in Python from plain spoken text.

![Alt Text](https://github.com/lazzm/CodeGPyT/blob/main/example.gif)

## How it works
The program reads plain English from an `input.txt` file, passes it to the OpenAI code model, generates code in Python, and automatically runs it using `exec`. The generated code is then saved into a folder called `generated_code` with a timestamp as the filename. The API key for OpenAI is stored in a `.env` file in the same location as `main.py`. There is an `env.example` file provided which contains `OPENAI_API_KEY=` that can be copied and named `.env` and filled in with your API key.

## Installation
1. Clone the repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Copy the `.env.example` file and rename the new one `.env`
4. Fill in the API key in the `.env`. Example: OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
5. Write the plain English description of what you want the code to do in the `input.txt` file. (I have left my example I used for fun in the text file)
6. Run `main.py`

## Note
The generated code may not always work as expected. It is recommended to review and test the generated code before using it in a production environment.

I use VS Code and have set main as the run configuration so I just edit the text file, save, and hit run.

