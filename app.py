import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={
    'Content-Type':'application/json'
}

history=[]

def generate_response(prompt):
    history.append(prompt)
    current_prompt="\n".join(history)

    data={
        "model":"CodeAssist",
        "prompt":current_prompt,
        "stream":False
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        model_response=data['response']
        return model_response
    else:
        print("error:",response.text)

interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="How can I assist?"),
    outputs="text"
)

interface.launch()