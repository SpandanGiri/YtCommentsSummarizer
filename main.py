import  ollama 

comments = ['nice video','quite informative','need more of this','your lectures are truly amazing']

chat_prompt = '''Hi I will provide you with some comments of youtube video , understand each comment and give me a summarized verison
using the comments do not add extra information other than from the comments

Here are the following comments:

'''

for comment in comments:
    chat_prompt = chat_prompt + '\n' + comment


print(chat_prompt)

response = ollama.chat(model='llama3.2',messages=[{"role":"user","content":chat_prompt}])

print("Summarized comments are :")
print(response.message.content)
