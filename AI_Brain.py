# AI_Brain.py
import random
from datetime import datetime

def generate_signal():
    # Simulate basic signal logic using time and randomness
    hour = datetime.now().hour
    if hour < 12:
        base_signal = "BUY"
    elif 12 <= hour < 16:
        base_signal = "HOLD"
    else:
        base_signal = "SELL"

    noise = random.choice(["BUY", "SELL", "HOLD"])
    final_signal = random.choice([base_signal, noise])
    return final_signal
