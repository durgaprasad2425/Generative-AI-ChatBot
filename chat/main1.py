import pickle
import google.generativeai as palm



def load_model(filepath):
    with open(filepath, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    return loaded_model

def generate_response(user_input, loaded_model):
    greeting_prompt = "Hi there! I'm Claude, your employee onboarding assistant."
    prompt = f" {greeting_prompt} exit{user_input}"
    
    completion = palm.generate_text(
        model=loaded_model,
        prompt=prompt,
        temperature=1.0,
        max_output_tokens=800,
    )

    return completion.result

def main():
    filepath = 'onboarding model.pkl'
    palm.configure(api_key='')  # Assuming you have a valid configuration here

    # Load the model
    loaded_model = load_model(filepath)
        # Initial greeting from the chatbot
    #initial_greeting = "Hi there! I'm Claude, your employee onboarding assistant."
    #print("Chatbot:", initial_greeting)


    # Example conversation loop
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break

        response = generate_response(user_input, loaded_model)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()


