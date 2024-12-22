from recorder import ScreenRecorder

if __name__ == "__main__":
    recorder = ScreenRecorder('output.avi')

    recording_duration = float(input("Enter recording duration in seconds: "))
    recorder.record_screen(recording_duration)