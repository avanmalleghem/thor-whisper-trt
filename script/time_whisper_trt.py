import argparse
import time

from whisper_trt import load_trt_model
from whisper.model import disable_sdpa

parser = argparse.ArgumentParser()
parser.add_argument("--speech", required=True)

args = parser.parse_args()

with disable_sdpa():
    model = load_trt_model("base.en")
    
    # we do a first inference to "warm" the model
    result = model.transcribe(args.speech)
    
    t0 = time.time()
    result = model.transcribe(args.speech)
    print(result['text'])
    t1 = time.time()
    total = t1-t0
    print(f"Transcription took {total} seconds")

