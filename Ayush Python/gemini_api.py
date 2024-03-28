import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display  # Not necessary for core functionality
from IPython.display import Markdown  # Not necessary for core functionality

import os

GENAI_API_KEY = os.getenv('GET-API-KEY')
genai.configure(api_key='GET-API-KEY')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')
question = input('Ask a question to your rome friend: ')
response = model.generate_content("Answer me like a rome centurion is smart and is flexing it  "+question)

# to_markdown(response.text)
print(response.text)
