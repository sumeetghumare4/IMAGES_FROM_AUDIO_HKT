import os

# AssemblyAI API
UPLOAD_ENDPOINT = 'https://api.assemblyai.com/v2/upload'
TRASCRIPT_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
AUTHORIZATION_KEY = '2a8d7f05cc4d41c0ad1f1f72618a4ead'

# Stability API
STABILITY_KEY = 'sk-x1K5bl7rNCGx6pXF0cJUHcduT05q57IvpHMPiVK2GsYHYF9h'

# The Root Directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')

OUT_DIR = os.path.join(ROOT_DIR, 'output/')
RECORDING_DIR = os.path.join(OUT_DIR, 'recording')
IMAGE_DIR = os.path.join(OUT_DIR, 'images')

WAVE_OUTPUT_FILE = os.path.join(RECORDING_DIR, "recorded.wav")
IMAGE_OUPUT_FILE = os.path.join(IMAGE_DIR, "image.jpg")
CONGIF_FILE = os.path.join(ROOT_DIR,'src/config.ini')

# Audio configurations
INPUT_DEVICE = 0
MAX_INPUT_CHANNELS = 1  # Max input channels
DEFAULT_SAMPLE_RATE = 44100   # Default sample rate of microphone or recording device
DURATION = 10   # 3 seconds
CHUNK_SIZE = 1024