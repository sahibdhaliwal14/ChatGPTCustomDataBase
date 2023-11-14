from pypdf import PdfReader
import pypdf
from llama_index import StorageContext
from llama_index import load_index_from_storage
from llama_hub.file.base import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex
from llama_index import download_loader
import os
import openai
import config
api_key = config.DevelopmentConfig.OPENAI_KEY
os.environ['api-key-here'] = api_key
SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
loader = SimpleDirectoryReader('put-folder-path-here', recursive=True, exclude_hidden=True)
documents = loader.load_data()
openai.api_key = 'put-your-api-key-here'
index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir='put-your-folder-path-here')
index = load_index_from_storage(StorageContext.from_defaults(persist_dir='put your folder path here - example folder path:/home/sahib/data'))
