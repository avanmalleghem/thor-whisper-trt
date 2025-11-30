import torch, platform
print("PyTorch CUDA:", torch.version.cuda)
print("torch build:", torch.__version__)
print("GPU detected:", torch.cuda.device_count())
try:
    import tensorrt as trt
    print("TensorRT:", trt.__version__)
except Exception as e:
    print("TensorRT import failed:", e)