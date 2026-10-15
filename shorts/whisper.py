import sys, json
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]
import subprocess, numpy as np
raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout
audio = np.frombuffer(raw, np.float32)
m = WhisperModel("small.en", device="cpu", compute_type="int8")
seg, info = m.transcribe(audio, word_timestamps=True, vad_filter=False, language="en")
W = []
for s in seg:
    for w in s.words:
        W.append({"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)})
json.dump(W, open(out, "w"))
print(len(W), "palavras", info.duration, "s")
