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
model_dir = "models/xtts_v2"  # directory, not .pth
config_path = os.path.join(model_dir, "config.json")
speaker_wav_path = "voice_sample.wav"
output_file = "output/cloned_speech.wav"

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
tts = TTS(model_path=model_dir, config_path=config_path, progress_bar=True, gpu=False)

# ------------------------
# Output folder
# ------------------------
os.makedirs("output", exist_ok=True)

# ------------------------
# Select speaker if multi-speaker
# ------------------------
speaker_arg = None
if hasattr(tts, "speakers") and tts.speakers:
    speaker_arg = list(tts.speakers.keys())[0]

# ------------------------
# Run speech synthesis
# ------------------------
tts_args = {
    "text": "Hello! This is a voice cloned with XTTS running in GitHub Actions.",
    "file_path": output_file,
    "language": "en"
}

if os.path.isfile(speaker_wav_path):
    tts_args["speaker_wav"] = speaker_wav_path
elif speaker_arg:
    tts_args["speaker"] = speaker_arg

tts.tts_to_file(**tts_args)

print(f"✅ Speech synthesis finished. Check {output_file}")
