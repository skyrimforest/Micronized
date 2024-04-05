
FROM python:3.10

# 设置时区为上海
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

WORKDIR /app

# 安装opencv依赖项
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY ./requirements.txt /app/requirements.txt

RUN pip install  -i https://pypi.mirrors.ustc.edu.cn/simple --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/Pro01Preprocessor

EXPOSE 12003

CMD ["python","./Pro01Preprocessor/main.py"]

