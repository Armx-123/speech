import os
import torch
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig  # <-- add this

# Auto-accept licenses
os.environ["TTS_AUTO_ACCEPT"] = "1"

# Paths
model_dir = "models/xtts_v2"
config_path = os.path.join(model_dir, "config.json")
model_path = model_dir

# Register all safe globals required by XTTS checkpoint
torch.serialization.add_safe_globals([XttsConfig, XttsAudioConfig])

# Initialize TTS
tts = TTS(model_path=model_path, config_path=config_path, progress_bar=True, gpu=False)

# Output folder
os.makedirs("output", exist_ok=True)

# Run speech synthesis
tts.tts_to_file(
    text="Hello! This is a voice cloned with XTTS running in GitHub Actions.",
    speaker_wav="voice_sample.wav",
    file_path="output/cloned_speech.wav"
)
