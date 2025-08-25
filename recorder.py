import sounddevice as sd
import wavio as wv
import datetime
import platform
import config

def get_device_id_by_name(name):
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if name.lower() in device['name'].lower():
            return i
    return None

freq = 44100
duration = 5  # in seconds
print('Started Recording')

# Determine the audio device to use. A custom device name can be supplied via
# the ``AUDIO_DEVICE_NAME`` environment variable. If not provided, choose a
# sensible default based on the platform.
device_name = config.AUDIO_DEVICE_NAME
if not device_name:
    if platform.system() == "Darwin":
        device_name = "Blackhole 2ch"
    elif platform.system() == "Windows":
        device_name = "CABLE Output"

device_id = get_device_id_by_name(device_name) if device_name else None

if device_id is None:
    available = ", ".join([d['name'] for d in sd.query_devices()])
    print(f"Audio device '{device_name}' not found. Available devices: {available}")
    exit(1)

while True:
    ts = datetime.datetime.now()
    filename = ts.strftime("%Y-%m-%d %H:%M:%S")

    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1, device=device_id)

    # Record audio for the given number of seconds
    sd.wait()

    # Convert the NumPy array to audio file
    wv.write(f"./recordings/{filename}.wav", recording, freq, sampwidth=2)

