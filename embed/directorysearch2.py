from llama_hub.file.base import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex
from llama_index import download_loader
from pypdf import PdfReader
import pypdf
SimpleDirectoryReader = download_loader("SimpleDirectoryReader")



import os
import config 
import openai 

os.environ['api-key-here'] = config.KEY

openai.api_key = 'api-key-here'
openai.api_key = os.getenv('api-key-here')

loader = SimpleDirectoryReader('folder path here', recursive=True, exclude_hidden=True)
documents = loader.load_data()
openai.api_key = 'api-key-here'
index = GPTVectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()



