import os
from TTS.api import TTS

os.environ["TTS_AUTO_ACCEPT"] = "1"

# Path to the unzipped XTTS model
model_path = "models/xtts_v2"

tts = TTS(model_path)

# Example text to synthesize
text = "Hello! This is a test of XTTS voice cloning in GitHub Actions using the release sample."

# Output directory
os.makedirs("output", exist_ok=True)

# Use the downloaded voice sample from release
tts.tts_to_file(
    text=text,
    speaker_wav="voice_sample.wav",  # Sample voice from release
    file_path="output/cloned.wav"
)
