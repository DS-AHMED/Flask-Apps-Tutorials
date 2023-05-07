import openai
from typing import List, Dict

# Load OpenAI API key from configuration or environment variable
OPENAI_API_KEY = 'insert openai key here'
openai.api_key = OPENAI_API_KEY

# Choosing the used model
MODEL_ID = 'gpt-3.5-turbo'

def generate_chat_response(conversation: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Generates a chat response from OpenAI GPT-3 model given a conversation.

    Args:
        conversation: A list of dictionaries representing the conversation. Each dictionary contains
                      two keys: 'role' for the speaker's role and 'content' for the message content.

    Returns:
        A list of dictionaries representing the updated conversation with the latest response from the model.
    """
    response = openai.ChatCompletion.create(model=MODEL_ID, messages=conversation)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation
