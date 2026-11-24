# SIH26172 — Edge Voice Activator — MVP v2

This version fixes the earlier prototype: the START button now starts
real microphone capture and offline wake-phrase recognition.

## Important

The current MVP uses **Vosk** for offline speech recognition and checks
for the phrase **"Hey ISRO"**.

This is an intermediate proof-of-concept, not yet the final TinyML model.
The final SIH implementation should replace Vosk phrase matching with
a dedicated quantized wake-word classifier trained for "Hey ISRO".

## 1. Install packages

Open the VS Code terminal:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\activate
pip install -r requirements.txt
```

## 2. Download the offline Vosk model

Download:

**vosk-model-small-en-us-0.15**

from the official Vosk models page:
https://alphacephei.com/vosk/models

Extract it so the folder is exactly:

```text
SIH26172_Voice_Activator_v2
└── ml
    └── model
        └── vosk-model-small-en-us-0.15
            ├── am
            ├── conf
            ├── graph
            ├── ivector
            └── ...
```

Do NOT put the ZIP file there without extracting it.

## 3. Run

```powershell
python app.py
```

Click **START MICROPHONE** and say:

```text
Hey ISRO
```

The application should show:

```text
✓ WAKE WORD DETECTED
```

## 4. If the microphone is not detected

Check Windows:
Settings → Privacy & security → Microphone

Enable microphone access for desktop apps.

## 5. Next development stage

After this MVP works:

1. Collect "Hey ISRO" positive and negative audio
2. Extract log-Mel/MFCC features
3. Train a small wake-word classifier
4. Quantize to INT8
5. Measure false accepts, false rejects, latency and model size
6. Deploy with TFLite Micro on ESP32-S3 if hardware becomes available
