import os
from TTS.api import TTS

# Pick an English-only model (no multilingual)
english_models = [
    "tts_models/en/ljspeech/tacotron2-DDC",
    "tts_models/en/ljspeech/glow-tts",
    "tts_models/en/ljspeech/fast_pitch",
    "tts_models/en/vctk/vits",  # multi-speaker English
]

output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

sample_text = "Hello! This is a test of English text to speech using Coqui TTS."

for model_name in english_models:
    print(f"[+] Loading {model_name} ...")
    tts = TTS(model_name)

    # pick first speaker if multi-speaker model
    kwargs = {}
    if tts.speakers:
        kwargs["speaker"] = tts.speakers[0]

    output_path = os.path.join(output_dir, f"{model_name.replace('/', '_')}.mp3")
    print(f"[+] Saving to {output_path}")
    tts.tts_to_file(text=sample_text, file_path=output_path, **kwargs)

print("[✓] Done! Check the outputs folder.")
