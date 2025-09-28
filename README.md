# Live DDoS Attack Map

A real-time DDoS attack visualization map showing Layer 7 attacks across countries. The map displays animated arcs representing attacks, with glowing dots traveling along curved paths.

## Features

- Real-time simulation of attacks.
- Randomized attack origin, target, and magnitude.
- Animated arcs with moving dots to represent attack traffic.
- Glow and pulse effects for better 3D appearance.
- Supports multiple countries with dynamic animations.
- Frontend served directly from FastAPI.

## Requirements

- Python 3.10+
- Packages listed in `requirements.txt`.

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```
Install required Python modules:
```bash
pip install -r requirements.txt
```
   Set your Cloudflare API token (optional if you want real attack data):
```bash
export CLOUDFLARE_API_TOKEN="your_token_here"   # Linux/macOS
set CLOUDFLARE_API_TOKEN=your_token_here        # Windows
```

# Dependencies

Python packages:

    fastapi
    httpx
    apscheduler
    uvicorn
    python-dotenv (optional, if using .env files for API token)

Frontend libraries (included via CDN):

    Leaflet.js
    Leaflet.curve plugin

Notes

    The animation generates random attacks every few seconds while letting old attacks finish.
    You can adjust refreshAttacks interval or animation duration in static/script.js for smoother effects.
    For real attack data, ensure the Cloudflare API token is valid and fetch function is enabled.

