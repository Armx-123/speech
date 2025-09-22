import os
from TTS.api import TTS

# Use the environment variable to auto-accept the license
os.environ["TTS_AUTO_ACCEPT"] = "1"

# Point directly to your local model folder (unzip your xtts_v2.zip into this path)
model_path = "models/xtts_v2"

# Initialize TTS with the local folder, not a model name
tts = TTS(model_path, progress_bar=True)

# Example: generate speech from text using a voice sample
output_file = "output/cloned_speech.wav"
os.makedirs("output", exist_ok=True)
tts.tts_to_file(text="Hello! This is a test of the cloned voice.", speaker_wav="voice_sample.wav", file_path=output_file)
