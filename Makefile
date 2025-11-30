.PHONY: build
build:
	docker build -t thor-whisper-trt:latest .

.PHONY: run
# ipc and ulimit parameters are to avoid a warning when starting
run:
	docker run --runtime=nvidia -v=./cache:/root/.cache/whisper \
			   -v=./cache:/root/.cache/whisper_trt -v=./speech:/workspace/speech \
			   -v=./script:/workspace/script --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -it \
			   --rm thor-whisper-trt:latest