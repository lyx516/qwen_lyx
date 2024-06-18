# 项目名称:

qwen_lyx

## 简介:
本项目为纯个人使用，基于qwen—72B项目（由阿里云开源），使用DashScope API 进行对话和回复，主要实现了终端接受流式信息，并进行多轮对话。下图转为gif后自动慢放了，实际响应速度要快得多。

![image](https://github.com/lyx516/qwen_lyx/blob/main/assets/1.gif)

## 文件说明:

### qwen72B.py

这是项目的主要脚本文件，用于在终端上执行。您可以使用以下命令运行它：

```bash
python /your_path/qwen72B.py
```

请确保替换路径 /your_path/qwen72B.py 为实际的文件路径。这个脚本文件包含了与DashScope API交互的功能，并处理对话交互逻辑。
### api_key.txt
您需要手动添加DashScope API密钥到 api_key.txt 文件中。（注意：请不要将 api_key.txt 文件提交到 Git 仓库中。）
请确保将其放在与 qwen72B.py 同一目录下。
百炼aip申请可以到[阿里云百炼官网](https://bailian.console.aliyun.com/),个人用户的话价格相当便宜，而且有几百万字的试用

### chat.sh

这是用于在终端上运行 qwen72B.py 脚本的脚本文件。请设置其中路径为你的路径qwen72B.py文件路径，建议以软连接形式添加至环境变量中。
```bash
# 帮助信息
function usage() {
    echo "用法: $0 [-h] [-s] [-m] [-o]"
    echo "  -h    显示帮助信息"
    echo "  -s    将对话保存为Markdown文件"
    echo "  -o    在保存文件后自动打开文件"
    exit 1
}
```

## 安装
为了运行这个项目，您需要安装DashScope包。您可以使用以下命令安装它：

pip install dashscope
```
## 运行
在准备好DashScope API密钥和安装了DashScope包之后，您可以运行 qwen72B.py 脚本，并输入您的问题或指令以开始对话。当您输入 \q 时，对话将结束。
```
python /your_path/qwen72B.py
```
若你已经把qwen.sh脚本添加到环境变量中，可以直接运行：(像上方动图所展示的那样)
```bash
qwen
```
