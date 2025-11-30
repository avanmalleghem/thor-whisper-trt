FROM nvcr.io/nvidia/pytorch:25.08-py3

RUN apt-get update && \
    apt-get install -y \
    ffmpeg && \
    rm -rf /var/lib/apt/lists/*

RUN pip install openai-whisper onnx-graphsurgeon

# install whisper_trt
RUN git clone https://github.com/NVIDIA-AI-IOT/torch2trt && \
    cd torch2trt && \
    python3 setup.py install && cd .. && rm -rf torch2trt && \
    git clone https://github.com/NVIDIA-AI-IOT/whisper_trt.git && \
    cd whisper_trt && \
    python3 setup.py install && cd .. && rm -rf whisper_trt