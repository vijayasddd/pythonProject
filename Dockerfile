# 使用一个python3镜像作为基础镜像
FROM python:3.11.4-slim-bullseye

# 设置工作目录为/app
WORKDIR /app

# 将当前目录下的所有文件复制到容器的/app目录下
COPY . /app

# 安装依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露端口
EXPOSE 5001

# 启动应用
CMD ["python", "app.py"]