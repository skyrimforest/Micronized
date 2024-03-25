# Docker file for rabbitmq single or cluster from bolingcavalry 
# VERSION 0.0.1
# Author: skyrim
# Time: 2024/3/7
#!/bin/bash
sudo docker run -d --hostname myrabbit --name rabbittest -e RABBITMQ_DEFAULT_USER=skyrim -e RABBITMQ_DEFAULT_PASS=111111 -p 5672:5672 -p 15672:15672 rabbitmq:3-management

# 使用官方的 RabbitMQ 镜像作为基础镜像
#FROM rabbitmq:3.8

# 设置环境变量
#ENV RABBITMQ_DEFAULT_USER=admin
#ENV RABBITMQ_DEFAULT_PASS=password

# 暴露 RabbitMQ 默认端口
#EXPOSE 5672 15672
