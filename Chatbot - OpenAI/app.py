import os
import asyncio
from functools import wraps
from flask import Flask, render_template, jsonify, request
import aiapi


app = Flask(__name__)

# initiating conversation with the model
conversation = [{'role': 'system', 'content': 'How may I help you?'}]
conversation = aiapi.generateChatResponse(conversation)


def async_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, func, *args, **kwargs)
    return wrapper


@app.route('/', methods=['POST', 'GET'])
async def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        conversation.append({'role': 'user', 'content': prompt})
        conversation1 = conversation.copy()
        conversation1 = await async_handler(aiapi.generateChatResponse)(conversation1)
        res = {'answer': conversation1[-1]['content'].strip()}
        return jsonify(res), 200

    return render_template('index.html', **locals())


if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', '8888')
    app.run(host=host, port=port, debug=True)
