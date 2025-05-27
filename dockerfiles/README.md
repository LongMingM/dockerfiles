# USE CODE
docker run --gpus all --rm -it -v .:/app --name test imageclass:latest /bin/bash
##挂载服务器上需要多分配内存
docker run --gpus all --shm-size=8g --rm -it -v .:/app --name test imageclass:latest /bin/bash
--ipc=host
docker run --gpus all --ipc=host --rm -it -v .:/app --name test imageclass:latest /bin/bash

# SAVE IMAGES
docker save -o my_image.tar your_image_name:tag
# LOAD IMAGES
docker load -i my_image.tar


# LOG
20250521：add imageClass_pytorch2.7.0_cuda11.8_cudnn9_runtime
20250520: add tensorflow2.17.0-gpu



