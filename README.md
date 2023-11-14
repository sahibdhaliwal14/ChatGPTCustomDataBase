# ChatGPTCustomDataBase
Created my own chatGPT interface which connects to a local directory folder that is used as the database for this custom chatGPT interface.  

There are 4 parts to the set up follow all parts:

Part 1:
Please go through all files in all folders(chatgpt & embed) and add your api key as well as path to directory...
... in the varibles for the api key and path to directory. (path to directory example - /home/sahib/data )
.. please keep in mind you will either have to make a folder and specify the path or specify an existing folders path

Part 2:
First of all you will need to install these via pip install to get the environment set up:
pip install virtualenv
pip install flask
pip install openai
pip install llama-index
pip install llama-hub
pip install nltk
pip install pypdf

Part 3:
You will need to make 2 directories (keep in mind these directories are currently in the repository, they are just empty)
1.) the first will be in the directory \ChatGPTCustomDataBase\chatgpt, you will have to create a virtual environment directory called \ChatGPTCustomDataBase\chatgpt\chatgptenv
    - to do so do the follow commands (via linux machine)
    - in the \ChatGPTCustomDataBase\chatgpt directory..
    - mkdir chatgptenv... from there run the command
    -.. virtualenv /path/to/chatgpt/chatgptenv
    -

2.) The second will be in the directory \ChatGPTCustomDataBase\embed, you will have to create a virtual environment directory called \ChatGPTCustomDataBase\embed\embedenv
  - to do so do the follow commands (via linux machine)
  - in the \ChatGPTCustomDataBase\embed directory..
  - mkdir embedenv... from there run the command
  - virtualenv /path/to/chatgpt/embedenv

Part 4:
You will need to activate both virtual environments and then run 2 python scripts to get the interface launched
  Open a command prompt/terminal 
  - first: cd embed
  - run the command: source embedenv/bin/activate
  - then run the command: python directorysearch2.py
  -  directorysearch2.py is the python script that connects the specified local directory folder and you api key together to get the interface ready for use

Now in another command terminal/terminal 
  -  second: cd chatgpt
  -  run the command chatgptenv/bin/activate
  -  run the command: cd chat-gpt
  -  run the command: python app.py
  -  app.py is the python script that launches the interface via local server on an html page

  -  Keep in mind when launching the app.py pyhton script you made need to open port 8888..
  -  .. this document will be updated shortly to include the commands to do so 
