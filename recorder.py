import pyautogui
import numpy as np
import cv2
import time


def capture_screen():
    try:
        screenshot = pyautogui.screenshot()
        return screenshot
    except Exception as e:
        print(f"Error capturing screen: {e}")
        return None


def screenshot_to_array(screenshot):
    try:
        return np.array(screenshot)
    except Exception as e:
        print(f"Error converting screenshot to array: {e}")
        return None


class ScreenRecorder:
    def __init__(self, output_file, fps=20.0):
        self.output_file = output_file
        self.fps = fps
        self.frames = []
        self.is_recording = False

    def write_video(self):
        try:
            height, width, _ = self.frames[0].shape
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(self.output_file, fourcc, self.fps, (width, height))

            for frame in self.frames:
                out.write(frame)

            out.release()
        except Exception as e:
            print(f"Error writing video: {e}")

    def record_screen(self, duration):
        print("Recording started...")
        self.is_recording = True
        start_time = time.time()
        end_time = start_time + duration
        frame_interval = 1 / self.fps

        while time.time() < end_time:
            frame_start_time = time.time()
            screenshot = capture_screen()
            if screenshot is not None:
                frame = screenshot_to_array(screenshot)
                if frame is not None:
                    self.frames.append(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            frame_end_time = time.time()
            time_to_sleep = frame_interval - (frame_end_time - frame_start_time)
            if time_to_sleep > 0:
                time.sleep(time_to_sleep)

        self.write_video()
        self.is_recording = False
        print("Recording complete.")