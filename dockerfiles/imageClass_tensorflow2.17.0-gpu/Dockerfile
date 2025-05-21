FROM tensorflow/tensorflow:2.17.0-gpu
WORKDIR /app

COPY requirements.txt /app/


# 安装所有编译工具和 OpenCV 运行时依赖，以及 python3-pip
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        git \
        zip \
        curl \
        htop \
        libgl1 \
        libglib2.0-0 \
        libpython3-dev \
        gnupg \
        g++ \
		jupyter \
        libusb-1.0-0 \
        build-essential \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

   
# 升级 pip 并安装 Python 依赖
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

# 4. 再把其余源码拷贝进来
COPY . /app

# 5. （可选）暴露端口，视你的应用而定
# EXPOSE 8888

# 6. 默认启动命令（以你的测试脚本或训练脚本为准）
CMD ["python3", "test_tensorflow.py"]