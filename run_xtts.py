import os

# Auto-accept Coqui CPML license
os.environ["TTS_AUTO_ACCEPT"] = "1"

from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False)
tts.tts_to_file(
    text="Hello! This is a test of my cloned voice on GitHub Actions.",
    speaker_wav="voice_sample.wav",
    language="en",
    file_path="cloned.wav"
)
