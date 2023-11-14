from flask import Flask, render_template, jsonify, request
import config
import openai
import aiapi
import os

from llama_index import GPTVectorStoreIndex
from llama_index import StorageContext
from llama_index import load_index_from_storage
from llama_hub.file.base import SimpleDirectoryReader
from llama_index import download_loader


os.environ['put-your-api-key-here'] = config.DevelopmentConfig.OPENAI_KEY

#create index for /data directory
ind = load_index_from_storage(StorageContext.from_defaults(persist_dir='add-your-folder-path-here'))

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'POST':
       
       prompt = request.form['prompt']
    
       res = {}
       query_engine = ind.as_query_engine()
       r = query_engine.query(prompt) 
       res['answer'] = r.response 
       #res['answer'] = aiapi.generateChatResponse(prompt)
       return jsonify(res), 200



    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)

