import boto3
from langchain_community.llms import Bedrock
from langchain.prompts import ChatPromptTemplate

client = boto3.client("bedrock-runtime", region_name="us-east-1")
 
model = Bedrock(client=client, model_id="anthropic.claude-v2:1")

prompt = ChatPromptTemplate.from_template("Does chemical bonding involve the process by which atoms combine to form molecules? Don't give summary just tell yes or no.")
 
chain = prompt | model

prediction = chain.invoke({})
print(prediction)
