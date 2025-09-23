import os
from TTS.api import TTS

# Auto-accept license (so it won’t hang in CI)
os.environ["TTS_AUTO_ACCEPT"] = "1"

# Local model directory (unzipped from xtts_v2.zip in the workflow)
model_dir = "models/xtts_v2"

# Point TTS at the local model
tts = TTS(model_path=model_dir, progress_bar=True, gpu=False)

# Make sure output folder exists
os.makedirs("output", exist_ok=True)

# Run inference with your uploaded sample
tts.tts_to_file(
    text="Hello! This is a test of the cloned voice running on GitHub Actions.",
    speaker_wav="voice_sample.wav",
    file_path="output/cloned_speech.wav"
)
