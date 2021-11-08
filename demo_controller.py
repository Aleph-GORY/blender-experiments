import midi_controller
import time

schema = {
    1: lambda x: print("K1", x),
    2: lambda x: print("K2", x),
    3: lambda x: print("K3", x),
    4: lambda x: print("K4", x),
    5: lambda x: print("K5", x),
    6: lambda x: print("K6", x),
    7: lambda x: print("K7", x),
    8: lambda x: print("K8", x),
}

if __name__ == "__main__":
    is_connected = midi_controller.setup_controller(schema)
    try:
        while True:
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nTest finished")
