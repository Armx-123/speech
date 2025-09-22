from TTS.api import TTS
import os

model_path = "models/xtts_v2"

tts = TTS(model_path)

text = "Hello! This is a test of XTTS voice cloning in GitHub Actions using the release sample."

os.makedirs("output", exist_ok=True)

tts.tts_to_file(
    text=text,
    speaker_wav="voice_sample.wav",
    file_path="output/cloned.wav"
)
