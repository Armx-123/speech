import os
from TTS.api import TTS

# English-only models
english_models = [
    "tts_models/en/vctk/vits",         # multi-speaker English
    "tts_models/en/ljspeech/tacotron2-DDC",  # single-speaker (male)
]

output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

sample_text = "Hello! This is a test of English text to speech using Coqui TTS."

for model_name in english_models:
    print(f"[+] Loading {model_name} ...")
    tts = TTS(model_name)

    # Pick first male speaker if multi-speaker model
    speaker_to_use = None
    if tts.speakers:
        # Coqui TTS VCTK model has speaker IDs like "p225", "p226", etc.
        # Most male speakers IDs: "p225" to "p250" (example, you can adjust)
        # For simplicity, pick the first available
        for speaker in tts.speakers:
            if "p2" in speaker:  # crude way to pick male IDs in VCTK
                speaker_to_use = speaker
                break
        if not speaker_to_use:
            speaker_to_use = tts.speakers[0]  # fallback

    kwargs = {}
    if speaker_to_use:
        kwargs["speaker"] = speaker_to_use

    output_path = os.path.join(output_dir, f"{model_name.replace('/', '_')}_{kwargs.get('speaker','default')}.mp3")
    print(f"[+] Saving to {output_path}")
    tts.tts_to_file(text=sample_text, file_path=output_path, **kwargs)

print("[✓] Done! Check the outputs folder.")
