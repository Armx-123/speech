import os
from TTS.api import TTS

# Only English male models
# Single-speaker LJSpeech models are male by default
english_male_models = [
    "tts_models/en/ljspeech/tacotron2-DDC",
    "tts_models/en/ljspeech/glow-tts",
    "tts_models/en/ljspeech/fast_pitch"
]

output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

sample_text = "Hello! This is a test of English male voices using Coqui TTS."

for model_name in english_male_models:
    print(f"[+] Loading {model_name} ...")
    tts = TTS(model_name)

    # Single-speaker models, no speaker needed
    output_path = os.path.join(output_dir, f"{model_name.replace('/', '_')}.mp3")
    print(f"[+] Saving to {output_path}")
    tts.tts_to_file(text=sample_text, file_path=output_path)

print("[✓] Done! Check the outputs folder.")
