import os

USER_NAME = "JOHN"
AUDIO_GENERATION_ID = os.getenv("AUDIO_GENERATION_ID", "audio gen id has not been provided!")
TRANSCRIPT_FILE = "transcriptions/transcript.txt"

# Optional: override the name of the audio input device used by ``recorder.py``
# If not set, platform-specific defaults will be used.
AUDIO_DEVICE_NAME = os.getenv("AUDIO_DEVICE_NAME", "")
