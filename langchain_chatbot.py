import os
# import sys
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

APIKEY = "sk-drbU3fPxBt2Wj5KIJcT3BlbkFJQ1REKl2qHQCPELPZc753"
os.environ['OPENAI_API_KEY'] = APIKEY

query = input('enter your question: ')
print(query)

#loader = TextLoader('data.txt')
loader = DirectoryLoader('.', glob='*.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))
