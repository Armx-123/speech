import os
from TTS.api import TTS
import torch

# ------------------------
# Auto-accept Coqui license
# ------------------------
os.environ["TTS_AUTO_ACCEPT"] = "1"

# ------------------------
# Paths
# ------------------------
model_dir = "models/xtts_v2"
config_path = os.path.join(model_dir, "config.json")
# Use directory, not the .pth file
model_path = model_dir
speaker_wav_path = "voice_sample.wav"  # Optional, must exist and be valid WAV

# ------------------------
# Safe globals for PyTorch 2.6+
# ------------------------
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig

safe_globals = [XttsConfig, XttsAudioConfig, XttsArgs, BaseDatasetConfig]
torch.serialization.add_safe_globals(safe_globals)

# ------------------------
# Init TTS
# ------------------------
tts = TTS(model_path=model_path, config_path=config_path, progress_bar=True, gpu=False)

# ------------------------
# Output folder
# ------------------------
os.makedirs("output", exist_ok=True)

# ------------------------
# Run speech synthesis
# ------------------------
tts_args = {
    "text": "Hello! This is a voice cloned with XTTS running in GitHub Actions.",
    "file_path": "output/cloned_speech.wav",
    "language": "en"  # Required for multi-lingual models
}

# Add speaker_wav if it exists
if os.path.isfile(speaker_wav_path):
    tts_args["speaker_wav"] = speaker_wav_path

# If model is multi-speaker and speaker_wav not provided, pick first speaker
if "speaker_wav" not in tts_args and hasattr(tts, "speakers") and tts.speakers:
    tts_args["speaker"] = list(tts.speakers.keys())[0]

tts.tts_to_file(**tts_args)

print("✅ Speech synthesis finished. Check output/cloned_speech.wav")
