FROM pytorch/pytorch:2.7.0-cuda11.8-cudnn9-runtime

WORKDIR /app

ADD . /app

RUN pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["sh", "run.sh"]