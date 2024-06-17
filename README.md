# 项目名称:

qwen_lyx

## 简介:
本项目为纯个人使用，基于qwen—72B项目，使用DashScope API进行对话和回复。
可以实现在终端实现多轮对话。

## 文件说明:

### qwen72B.py

这是项目的主要脚本文件，用于在终端上执行。您可以使用以下命令运行它：

```bash
python /your_path/qwen72B.py
```

请确保替换路径 /your_path/qwen72B.py 为实际的文件路径。这个脚本文件包含了与DashScope API交互的功能，并处理对话交互逻辑。
### aip_key.txt
您需要手动添加DashScope API密钥到 aip_key.txt 文件中。（注意：请不要将 aip_key.txt 文件提交到 Git 仓库中。）
请确保将其放在与 qwen72B.py 同一目录下。
百炼aip申请可以到[阿里云百炼官网](https://bailian.console.aliyun.com/),个人用户的话价格相当便宜，而且有几百万字的试用

### qwen.sh

这是用于在终端上运行 qwen72B.py 脚本的脚本文件。请设置其中路径为你的路径qwen72B.py文件路径，建议以软连接形式添加至环境变量中。
## 安装
为了运行这个项目，您需要安装DashScope包。您可以使用以下命令安装它：
```
pip install dashscope
```
## 运行
在准备好DashScope API密钥和安装了DashScope包之后，您可以运行 qwen72B.py 脚本，并输入您的问题或指令以开始对话。当您输入 \q 时，对话将结束。
```
python /your_path/qwen72B.py
```
