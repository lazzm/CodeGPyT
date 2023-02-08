import openai
import os
import html
import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(input_text):

    prompt_text = ("Reply to this as code in Python.\n"
                   "Description of what this code should do:\n")

    prompt_text = prompt_text + "\n\n" + input_text + "\n\n"
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt_text,
        temperature=0,
        max_tokens=500,
        stop=["</code>"]
    )

    response_text = response['choices'][0]['text']
    response_text = response_text.split("<code>")[1].split("</code>")[0]
    code = html.unescape(response_text)
    return code

# Get user text from a text file
input = open("input.txt", "r").read()

print("Generating code...\n")
try:
    code = generate_response(input)
except Exception as e:
    print("This is the error: " + str(e))
    exit()

print("Code:\n")
print(code + "\n")

# save the file to the generated_code folder and name the file with the current date and time eg: 2021-05-01-12:00:00.py

file = open("generated_code/" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-").replace(".", "-") + ".py", "w")
file.write(code)
file.close()

print("Executing code...\n")
exec(code)