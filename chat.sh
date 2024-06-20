#!/bin/bash

# 设置默认参数
MODEL_NAME="qwen2-72b-instruct"
SEED_MIN=1
SEED_MAX=10000
RESULT_FORMAT="message"
STREAM=true
OUTPUT_IN_FULL=true
MAX_INPUT_LENGTH=1000
OUTPUT_MARKDOWN=false
OUTPUT_FILE="output.md"
USE_ALTERNATE_SCRIPT=false

# 打印帮助信息
usage() {
  echo "Usage: $0 [options]"
  echo "Options:"
  echo "  -m, --model MODEL_NAME        Set the model name (default: $MODEL_NAME)"
  echo "  -s, --seed-min SEED_MIN       Set the minimum seed value (default: $SEED_MIN)"
  echo "  -S, --seed-max SEED_MAX       Set the maximum seed value (default: $SEED_MAX)"
  echo "  -f, --format RESULT_FORMAT    Set the result format (default: $RESULT_FORMAT)"
  echo "  -t, --stream STREAM           Set stream option (default: $STREAM)"
  echo "  -o, --output OUTPUT_IN_FULL   Set output in full option (default: $OUTPUT_IN_FULL)"
  echo "  -l, --max-input MAX_INPUT_LENGTH Set maximum input length (default: $MAX_INPUT_LENGTH)"
  echo "  -M, --markdown OUTPUT_FILE    Output results in Markdown format to specified file"
  echo "  -L, --use-alternate           Enter long text with line breaks"
  echo "  -h, --help                    Display this help message"
}

# 解析命令行参数
while [[ "$#" -gt 0 ]]; do
  case $1 in
    -m|--model) MODEL_NAME="$2"; shift ;;
    -s|--seed-min) SEED_MIN="$2"; shift ;;
    -S|--seed-max) SEED_MAX="$2"; shift ;;
    -f|--format) RESULT_FORMAT="$2"; shift ;;
    -t|--stream) STREAM="$2"; shift ;;
    -o|--output) OUTPUT_IN_FULL="$2"; shift ;;
    -l|--max-input) MAX_INPUT_LENGTH="$2"; shift ;;
    -M|--markdown) OUTPUT_MARKDOWN=true; OUTPUT_FILE="$2"; shift ;;
    -L|--use-alternate) USE_ALTERNATE_SCRIPT=true; ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown parameter passed: $1"; usage; exit 1 ;;
  esac
  shift
done

# 导出参数为环境变量
export MODEL_NAME
export SEED_MIN
export SEED_MAX
export RESULT_FORMAT
export STREAM
export OUTPUT_IN_FULL
export MAX_INPUT_LENGTH

# 选择运行的Python脚本
if $USE_ALTERNATE_SCRIPT; then
  SCRIPT_PATH="/Users/liyuxuan/Applications/qwen/qwen72B_l.py"
else
  SCRIPT_PATH="/Users/liyuxuan/Applications/qwen/qwen72B.py"
fi

# 运行 Python 脚本并将结果输出为Markdown文件（如果启用）
if $OUTPUT_MARKDOWN; then
  /opt/homebrew/anaconda3/bin/python "$SCRIPT_PATH" | tee "$OUTPUT_FILE"
else
  /opt/homebrew/anaconda3/bin/python "$SCRIPT_PATH"
fi
