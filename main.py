# main.py
from AI_Brain import generate_signal
import time

print("🚀 AI Trading Agent Started")

while True:
    signal = generate_signal()
    print(f"[Signal] Market says: {signal}")
    time.sleep(10)  # wait 10 seconds before next signal
