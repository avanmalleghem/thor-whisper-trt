# Hardware-Optimized Whisper on Thor

This repository provides a Docker environment to run Whisper with and without TensorRT hardware acceleration on NVIDIA GPUs. It includes a ROS node aswell and the Docker image needed to run it.

## Dependencies

* [NVIDIA container toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)

## Quickstart without ROS

* Build the Docker image : `make build`
* Run the container and open a terminal inside it : `make run`
* Available scripts (in the `script` folder):
    * `test_config.py` : Verifies that your GPU is detected and the environment is correctly configured.
    * `time_whisper.py` : Runs Whisper inference (no hardware acceleration) on an audio file passed as argument.
    * `time_whisper_trt.py` : Runs hardware-optimized Whisper inference (TensorRT) on an audio file passed as argument.
* Publish a path to a speech to convert to text : `ros2 topic pub -1 /speech_path std_msgs/msg/String '{data: "/workspace/speech/harvard.wav"}'`

## Quickstart with ROS

* Build the Docker image : `make build`
* Run the container : `make run-ros`
* Open a terminal in the container : `make open-terminal` then listen to the text topic : `ros2 topic echo /text`
* Open a terminal in the container : `make open-terminal` then publish the path to your sound in the speech_path topic : `ros2 topic pub -1 /speech_path std_msgs/msg/String '{data: "/workspace/speech/harvard.wav"}'`

## Good to know
* The Docker image is based on [Pytorch 2.8](https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel-25-08.html).
* By default, we use the `base` Whisper model.
* The first inference run will include overhead because:
    1. Whisper model must be downloaded.
    2. If using TensorRT, the model will be converted and cached.
* I'm able to run this code on my laptop aswell but I mainly tested it on Thor.

## Benchmark

* On the 18 seconds long wav file called `harvard.wav` using Thor:

|             | Time (s) |
| ----------- | -------- |
| Whisper     | 0.65    |
| Whisper TRT | 0.3     |

## Additional Resources
* [Official NVIDIA resource for deeplearning with Pytorch](https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/running.html)
