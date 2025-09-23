import os
import torch
from TTS.api import TTS

# Import all classes used in XTTS checkpoints
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig

# Register all XTTS-related classes as safe globals (one-time fix)
torch.serialization.add_safe_globals([XttsConfig, XttsAudioConfig, XttsArgs, BaseDatasetConfig])

# Auto-accept licenses
os.environ["TTS_AUTO_ACCEPT"] = "1"

# Paths
model_dir = "models/xtts_v2"
config_path = os.path.join(model_dir, "config.json")
model_path = model_dir  # point to folder with model.pth inside

# Initialize TTS
tts = TTS(model_path=model_path, config_path=config_path, progress_bar=True, gpu=False)

# Output folder
os.makedirs("output", exist_ok=True)

# Run speech synthesis
tts.tts_to_file(
    text="Hello! This is a voice cloned with XTTS running in GitHub Actions.",
    speaker_wav="voice_sample.wav",
    file_path="output/cloned_speech.wav",
    language="en"  # <-- add the language code here
)

