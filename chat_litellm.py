from langchain_community.chat_models import ChatLiteLLM

chat = ChatLiteLLM(model="gpt-3.5-turbo")
messages = [{ "content": "What are the 3 key features of jenkins?","role": "user"}]
response = chat.invoke(messages)
print(type(response))
print(response)
print(response.content)
print(response.response_metadata)
print(response.id)