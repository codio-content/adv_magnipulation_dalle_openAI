import os
import openai
import secret
openai.api_key=secret.api_key

### CODIO SOLUTION BEGIN
prompts ="what is dadaism?"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompts,
  top_p=1,
  max_tokens=100)


print(response['choices'][0]['text'].strip())
## CODIO SOLUTION END