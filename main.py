import httpx
import time
from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def main_loop():
    while True:
        try:
            huk1 = httpx.get("https://raw.githubusercontent.com/colordicerigger/Whattt-/refs/heads/main/test.txt").content.decode("utf-8").strip()
            delete = httpx.delete(huk1)
            print("Response status:", delete.status_code)

            if delete.status_code == 204:
                print("Webhuk", huk1[33:55], "\n", "VIDOLBLEN🐷🐷🐖🐖")
            else:
                for dots in [".", "..", "..."]:
                    print("\rWaiting for new webknur " + dots + "   ", end="", flush=True)
                    time.sleep(0.4)
                print("\r", end="", flush=True)

        except Exception as e:
            print("Error:", e)

        time.sleep(1)

# Run main_loop in background thread
threading.Thread(target=main_loop).start()

# Run Flask app in main thread (this is what Replit expects)
app.run(host='0.0.0.0', port=8080)
