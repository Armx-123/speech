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
model_path = model_dir  # Directory instead of .pth
speaker_wav_path = "voice_sample.wav"

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
# Pick speaker for multi-speaker models
# ------------------------
speaker_arg = None
if hasattr(tts, "speakers") and tts.speakers:
    speaker_arg = list(tts.speakers.keys())[0]

# ------------------------
# Run speech synthesis
# ------------------------
if os.path.isfile(speaker_wav_path):
    tts.tts_to_file(
        text="Hello! This is a voice cloned with XTTS running in GitHub Actions.",
        file_path="output/cloned_speech.wav",
        language="en",
        speaker_wav=speaker_wav_path
    )
else:
    tts.tts_to_file(
        text="Hello! This is a voice cloned with XTTS running in GitHub Actions.",
        file_path="output/cloned_speech.wav",
        language="en",
        speaker=speaker_arg
    )

print("✅ Speech synthesis finished. Check output/cloned_speech.wav")
