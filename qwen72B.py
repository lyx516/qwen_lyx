#!/opt/homebrew/anaconda3/bin/python
import dashscope
import random
from http import HTTPStatus
from colorama import Fore, Style

# Constants
with open('/Users/liyuxuan/Applications/qwen/api_key.txt', 'r') as file:
    API_KEY = file.read()
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

input_count = 0


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
            print(s, end='', flush=True)  # Flush output to ensure it is displayed immediately
            s1 = s2

        # Append model's response to conversation history for next round
        if s2.strip():
            conversation_history.append({'role': 'assistant', 'content': s2})
        else:
            print("Error: Assistant response content length must be greater than 0.")

    except Exception as e:
        print(f'An error occurred: {e}')


def split_long_input(user_input, max_length):
    """Split long input into smaller chunks."""
    return [user_input[i:i + max_length] for i in range(0, len(user_input), max_length)]


if __name__ == '__main__':
    input_count = 0
    while True:
        if input_count == 0:
            user_input = input(f"\n{Fore.YELLOW}请输入您的问题或指令 (输入 {Fore.BLUE}'\\q'{Fore.YELLOW} 结束对话):{Style.RESET_ALL} ")
        else:
            user_input = input(f"{Fore.RED}>>{Style.RESET_ALL} ")

        if user_input.lower() == '\q':
            break\

        # Check and handle long inputs
        if len(user_input) > MAX_INPUT_LENGTH:
            chunks = split_long_input(user_input, MAX_INPUT_LENGTH)
            for chunk in chunks:
                call_api_with_history(chunk)
        else:
            call_api_with_history(user_input)

        input_count += 1
        print('')  # Add a newline after each response
