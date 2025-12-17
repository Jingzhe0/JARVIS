from multiprocessing import Process, Event
from engine.gesture import gesture_controller

gesture_process = None
stop_event = Event()

def start_gesture(mode=1):
    global gesture_process, stop_event

    if gesture_process is None or not gesture_process.is_alive():
        stop_event.clear()
        gesture_process = Process(
            target=gesture_controller,
            args=(stop_event, mode),
            daemon=True
        )
        gesture_process.start()
        return True
    return False

def stop_gesture():
    global gesture_process, stop_event

    if gesture_process and gesture_process.is_alive():
        stop_event.set()
        gesture_process.terminate()
        gesture_process = None
        return True
    return False
