import os
from TTS.api import TTS

# Auto-accept license
os.environ["TTS_AUTO_ACCEPT"] = "1"

# Paths to your local files
model_dir = "models/xtts_v2"
config_path = os.path.join(model_dir, "config.json")
model_path = os.path.join(model_dir, "model.pth")

# Initialize TTS with local model + config
tts = TTS(model_path=model_path, config_path=config_path, progress_bar=True, gpu=False)

# Ensure output directory
os.makedirs("output", exist_ok=True)

# Generate cloned voice
tts.tts_to_file(
    text="Hello! This is running fully offline on GitHub Actions.",
    speaker_wav="voice_sample.wav",
    file_path="output/cloned_speech.wav"
)
