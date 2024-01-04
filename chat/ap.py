from flask import Flask, render_template, request,jsonify

import pickle
import google.generativeai as palm
import numpy as np
app = Flask(__name__, template_folder='template')

palm.configure(api_key='')
# Use the palm.list_models function to find available models:
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def generate_response(user_input,model):
    greeting_prompt = "Hi there! I'm HGT Bot, your employee onboarding assistant."
    prompt = f" {greeting_prompt}{user_input} "
    
    completion = palm.generate_text(
        model="models/text-bison-001",
        prompt=prompt,
        temperature=0,
        max_output_tokens=100,
        candidate_count=1,
        
    )

    return completion.result

# Load the model when the app starts

#palm.configure(api_key='AIzaSyCSA456-F8GFwEJh4VdGSl1rFhsPD02N4o')  # Assuming you have a valid configuration here


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    
    if user_input.lower() in ['exit', 'quit', 'bye']:
        chatbot_response = "Goodbye!"
    else:
        chatbot_response = generate_response(user_input, model)
        return jsonify({'user_input': user_input, 'chatbot_response': chatbot_response})

    
    # return render_template('index.html', user_input=user_input, chatbot_response:chatbot_response)

if __name__ == '__main__':
    app.run(debug=True)
