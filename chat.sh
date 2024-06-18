#!/bin/bash

# 获取脚本所在目录的绝对路径
SCRIPT_DIR=$(cd $(dirname $0); pwd)
PYTHON_SCRIPT="/Users/liyuxuan/Applications/qwen/qwen72B.py"
LOG_FILE="$SCRIPT_DIR/conversation_history.md"

# 帮助信息
function usage() {
    echo "用法: $0 [-h] [-s] [-m] [-o]"
    echo "  -h    显示帮助信息"
    echo "  -s    将对话保存为Markdown文件"
    echo "  -m    使用Markdown文件格式保存对话"
    echo "  -o    在保存文件后自动打开文件"
    exit 1
}

# 参数解析
SAVE_MARKDOWN=false
OPEN_AFTER_SAVE=false
while getopts "hsmo" opt; do
    case ${opt} in
        h)
            usage
            ;;
        s)
            SAVE_MARKDOWN=true
            ;;
        m)
            SAVE_MARKDOWN=true
            ;;
        o)
            OPEN_AFTER_SAVE=true
            ;;
        *)
            usage
            ;;
    esac
done

# 运行Python脚本
if $SAVE_MARKDOWN; then
    python3 "$PYTHON_SCRIPT" | tee "$LOG_FILE"
    if $OPEN_AFTER_SAVE; then
        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            xdg-open "$LOG_FILE"
        elif [[ "$OSTYPE" == "darwin"* ]]; then
            open "$LOG_FILE"
        elif [[ "$OSTYPE" == "cygwin" ]]; then
            cygstart "$LOG_FILE"
        elif [[ "$OSTYPE" == "msys" ]]; then
            start "$LOG_FILE"
        elif [[ "$OSTYPE" == "win32" ]]; then
            start "$LOG_FILE"
        else
            echo "无法自动打开文件，请手动打开 $LOG_FILE"
        fi
    fi
else
    python3 "$PYTHON_SCRIPT"
fi
