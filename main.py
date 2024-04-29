from sense_hat import SenseHat
import time
import requests

hat = SenseHat()

orientation = hat.get_orientation_degrees()

# Hvad er følsomheden?
threshold = 30
max_threshold = 250

pitch = 0.0
roll = 0.0
yaw = 0.0

# tid siden programstart.
deltatime = 0.0

# antal kalkuleringer i sekundet.
framerate = 30

def set_orientation(o):
    global pitch, roll, yaw
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]


def sub_orientation(a, b):
    orientation = {
        "pitch": 0.0,
        "roll": 0.0,
        "yaw": 0.0,
    }
    
    orientation["pitch"] = b["pitch"] - a["pitch"]
    orientation["roll"] = b["roll"] - a["roll"]
    orientation["yaw"] = b["yaw"] - a["yaw"]
    return orientation


def crash(severity):
    jsonData = {"severity": severity}
    resp = requests.post("http://127.0.0.1:8080/crash", json = jsonData)
    print(resp.text)
    quit() 


while True:
    t = time.time()
    diff_orientation = sub_orientation(orientation, hat.get_orientation_degrees())

    if (
        (abs(diff_orientation["pitch"]) > threshold and abs(diff_orientation["pitch"]) < max_threshold) or
        (abs(diff_orientation["roll"]) > threshold and abs(diff_orientation["roll"]) < max_threshold) or
        (abs(diff_orientation["yaw"]) > threshold and abs(diff_orientation["yaw"]) < max_threshold)
        ):
            crash(10)
     
        
    orientation = hat.get_orientation_degrees()
    set_orientation(orientation)

    time.sleep(1 / framerate)
    print(orientation)
    # Calculation of delta time.
    diff = time.time() - t
    deltatime += diff
