import  ollama 
import backend.utils.scrapper as sc 


#url = "https://www.youtube.com/watch?v=T646W5pA6LE"

def commentsSummariszer(url):

    sc.scarp_comments(url)
    comments = sc.comments


    chat_prompt = '''Hi I will provide you with some comments of youtube video , understand each comment and give me a summarized verison of all the combined comments
    using the comments do not add extra information other than from the comments

    Here are the following comments:

    '''

    for comment in comments:
        chat_prompt = chat_prompt + '\n' + comment


    print(chat_prompt)

    response = ollama.chat(model='llama3.2',messages=[{"role":"user","content":chat_prompt}])

    return response.message.content
