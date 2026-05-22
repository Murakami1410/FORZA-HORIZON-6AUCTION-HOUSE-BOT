# FH6 Auction House Bot

An automated bot for the Forza Horizon 4 Auction House, built in Python.

## How it works

The bot monitors specific screen pixels to detect the game state and automatically simulates key presses to search and buy cars at the auction.

**Flow:**
1. Detects the search screen via the start pixel
2. Presses Enter to open the search
3. Presses Enter to confirm
4. Checks if a car was found via the result screen pixel
5. If found → presses Y, scrolls down, confirms the purchase
6. If not found → presses ESC and restarts

## Requirements

- Python 3.10+
- Resolution: 1720x1080 (default) — see the calibration section for other resolutions

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/fh4-auction-bot.git
cd fh4-auction-bot
```

**2. Create a virtual environment**
```bash
python -m virtualenv venv
venv\Scripts\activate.bat
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage

1. Open Forza Horizon 6
2. Go to Auction House → Search Cars
3. Set up your desired search filters
4. Run the bot:
```bash
python main.py
```
5. Quickly switch back to the game

## Calibration for other resolutions

If your resolution is different from 1720x1080, adjust the variables at the top of `main.py`:

```python
PIXEL_START   = (151, 662)      # Pixel on the search screen
PIXEL_CAR     = (382, 1015)     # Pixel on the result screen
COR_START     = (4, 4, 5)       # Expected color on the search screen
COR_CAR_FOUND = (255, 255, 255) # Color when a car is found
TOLERANCIA    = 20              # Allowed variation per RGB channel
```

## Disclaimer

This bot is for educational purposes only. The use of bots may violate the game's Terms of Service.
