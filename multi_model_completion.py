from litellm import completion
import boto3  
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

messages = [{ "content": "What are the 5 key features of jenkins?","role": "user"}]

# openai
response = completion(model="gpt-3.5-turbo", messages=messages)
print(response)
print("GPT-3.5-turbo: ", response['choices'][0]['message']['content'])

# bedrock
client = boto3.client("bedrock-runtime", region_name="us-east-1")
response = completion(model="bedrock/anthropic.claude-v2:1",messages = messages,aws_bedrock_client=client)
print(response)
print("Claude-V2:1: ", response['choices'][0]['message']['content'])

# azure openai
response = completion(model = "azure/lai-gpt-35-turbo", messages = messages)
print(response)
print("Azure OPENAI: ", response['choices'][0]['message']['content'])