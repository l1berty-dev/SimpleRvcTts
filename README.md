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
## Sources
The module was written using the following repositories

https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI

https://github.com/litagin02/rvc-tts-webui
