import os
from TTS.api import TTS

# Create output folder
output_dir = "tts_outputs"
os.makedirs(output_dir, exist_ok=True)

sample_text = "Hello, this is a test voice from Coqui TTS."

# Pick only a few models (to save time)
models = [
    "tts_models/en/ljspeech/tacotron2-DDC",
    "tts_models/en/vctk/vits",
    "tts_models/multilingual/multi-dataset/your_tts"
]

for model_name in models:
    print(f"Processing {model_name}...")
    tts = TTS(model_name)

    if tts.speakers:
        output_path = os.path.join(output_dir, f"{model_name.replace('/', '_')}_{tts.speakers[0]}.mp3")
        tts.tts_to_file(text=sample_text, speaker=tts.speakers[0], file_path=output_path)
    else:
        output_path = os.path.join(output_dir, f"{model_name.replace('/', '_')}.mp3")
        tts.tts_to_file(text=sample_text, file_path=output_path)

print("✅ Done! Files saved in tts_outputs/")
