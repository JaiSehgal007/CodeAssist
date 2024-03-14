# CodeAssist

CodeAssist is a Code assistant which is build using Codellama which is one of the state-of-art open-source model by Meta and Langchain for the backend and Gradio to create the user interface.

## Steps to reproduce the repository

1. to create virtual env
``` bash
python3 -m venv venv
```

2. to activate virtual env
``` bash
venv\Scripts\activate
```

3. Install dependencies from requirements.txt
``` bash
pip install -r requirements.txt
```

4. Install ollama by its exe file and pull codellama
``` bash
ollama pull codellama
```

5. creating model in ollama using after setting up the modelfile
``` bash
ollama create CodeAssist -f modelfile
```

6. To check if its running, run
``` bash
ollama run CodeAssist
```

7. Run the the app.py file
``` bash
python app.py
```
