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
model_path = os.path.join(model_dir, "model.pth")
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
# Patch GPT2InferenceModel to inherit GenerationMixin
# ------------------------
from TTS.tts.layers.xtts.gpt import GPT2InferenceModel
from transformers import GenerationMixin

class GPT2InferenceModelPatched(GPT2InferenceModel, GenerationMixin):
    pass

import TTS.tts.models.xtts as xtts_module
xtts_module.GPT2InferenceModel = GPT2InferenceModelPatched

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
    "language": "en",  # Required for multi-lingual models
    "speaker": "p225"  # Required for multi-speaker models, pick one from speakers_xtts.pth
}

# Add speaker_wav if it exists
if os.path.isfile(speaker_wav_path):
    tts_args["speaker_wav"] = speaker_wav_path

tts.tts_to_file(**tts_args)

print("✅ Speech synthesis finished. Check output/cloned_speech.wav")
