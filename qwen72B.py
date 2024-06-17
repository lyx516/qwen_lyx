import dashscope
import random
from http import HTTPStatus

# Constants
with open('/Users/liyuxuan/Applications/qwen/api_key.txt', 'r') as file:
    API_KEY = file.read()
MODEL_NAME = 'qwen1.5-72b-chat'
SEED_MIN = 1
SEED_MAX = 10000
RESULT_FORMAT = 'message'
STREAM = True
OUTPUT_IN_FULL = True

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

    # Add user input to conversation history
    conversation_history.append({'role': 'user', 'content': user_input})

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
            print(s, end='')
            s1 = s2

        # Append model's response to conversation history for next round
        conversation_history.append({'role': 'assistant', 'content': s2})

    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    while True:
        print("")
        user_input = input("请输入您的问题或指令 (输入 '\q' 结束对话): ")
        if user_input.lower() == '\q':
            break
        call_api_with_history(user_input)
        print('')  # Add a newline after each response
