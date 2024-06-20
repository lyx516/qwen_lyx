#!/opt/homebrew/anaconda3/bin/python
import dashscope
import random
from http import HTTPStatus
from colorama import Fore, Style
import sys

# Constants
with open('/Users/liyuxuan/Applications/qwen/api_key.txt', 'r') as file:
    API_KEY = file.read().strip()
MODEL_NAME = 'qwen2-72b-instruct'
SEED_MIN = 1
SEED_MAX = 10000
RESULT_FORMAT = 'message'
STREAM = True
OUTPUT_IN_FULL = True
MAX_INPUT_LENGTH = 1000  # 设置最大输入长度

# Set up DashScope API key
dashscope.api_key = API_KEY

# Initialize conversation history
conversation_history = []

def remove_common_prefix(s1, s2):
    """Remove the common prefix from two strings."""
    if s2.startswith(s1):
        return s2[len(s1):]
    else:
        return s2

def process_response(response):
    """Processes the API response and extracts the new content."""
    if response.status_code == HTTPStatus.OK:
        return response.output.choices[0]['message']['content']
    else:
        print(f'Request id: {response.request_id}, Status code: {response.status_code}, '
              f'error code: {response.code}, error message: {response.message}')
        return ''

def call_api_with_history(user_input):
    """Call the API with updated conversation history and handle the response."""
    global conversation_history

    # Process and send user input to the API
    if user_input.strip():
        conversation_history.append({'role': 'user', 'content': user_input})
    else:
        print("Error: User input content length must be greater than 0.")
        return

    try:
        responses = dashscope.Generation.call(
            MODEL_NAME,
            messages=conversation_history,
            seed=random.randint(SEED_MIN, SEED_MAX),
            result_format=RESULT_FORMAT,
            stream=STREAM,
            output_in_full=OUTPUT_IN_FULL
        )

        s1 = ''
        for response in responses:
            s2 = process_response(response)
            s = remove_common_prefix(s1, s2)
            print(s, end='', flush=True)
            s1 = s2

        if s2.strip():
            conversation_history.append({'role': 'assistant', 'content': s2})

    except Exception as e:
        print(f'An error occurred: {e}')

def read_multiline_input(prompt="请输入您的问题或指令（输入 '\\e' 结束对话）: "):
    print(prompt, end="", flush=True)
    user_input_lines = []
    while True:
        line = sys.stdin.readline()
        if line == '\n':  # Skip empty lines
            continue
        if line.strip() == '\\e':  # End input on '\\e'
            break
        user_input_lines.append(line.rstrip('\n'))  # Remove trailing newline
    return '\n'.join(user_input_lines)  # Join lines into single string

if __name__ == '__main__':
    while True:
        user_input = read_multiline_input()
        if user_input.lower().strip() == '\\q':
            print("对话已结束。")
            break

        # Process the multiline input
        call_api_with_history(user_input)
        print()  # Add a newline for separation