import openai

# Set up OpenAI API credentials
openai.api_key = "sk-proj-HuMbWINvafQ96sv9jLUsT3BlbkFJESwv7qk0dYz6SJFieRb4"

# Define the user's input (e.g. a question)
user_input = "What is the best way to learn Python?"

# Define the model and parameters for the response
model = "gpt-3.5-turbo"
temperature = 0.7

# Create a chat completion request
response = openai.ChatCompletion.create(
    model=model,
    messages=[
        {"role": "user", "content": user_input}
    ],
    temperature=temperature
)

# Print the response
print(response.choices[0].message)
