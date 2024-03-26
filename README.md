## Install
Make sure that you have Microsoft C++ Build Tools installed
```bash
git clone https://github.com/l1berty-dev/SimpleRvcTts.git
cd SimpleRvcTts

# Download models in root directory
curl -L -O https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt
curl -L -O https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt

cd ..

# Make virtual environment
python -m venv venv
# Activate venv (for Windows)
venv\Scripts\activate

# Install PyTorch manually if you want to use NVIDIA GPU (Windows)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

cd SimpleRvcTts

# Install requirements
pip install -r requirements.txt
```
## Tree
```
├── SimpleRvcTts #a ready-made module, I do not recommend changing the code
├── weights #folder with models
│   ├── model1
│   │   ├── my_model1.pth
│   │   └── my_index_file_for_model1.index
│   └── model2
│       ├── my_model2.pth
│       └── my_index_file_for_model2.index
└── main.py #this is your file where you can write code
...
```
## Example
```python
from SimpleRvcTts.tts import TTS

voice = TTS('new_myvoice', 'weights', 10, 'ru-RU-DmitryNeural-Male', 0.0, 'rmvpe', 1, 1)
info, data = voice.get('Это тестовый текст для проверки голоса')
voice.play(data) #playback of the final audio
voice.save(data, 'voice.wav') #saving a file by the specified path and name
```

## Sources
The module was written using the following repositories

https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI

https://github.com/litagin02/rvc-tts-webui
