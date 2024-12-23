from recorder import ScreenRecorder

if __name__ == "__main__":
    recorder = ScreenRecorder('output.avi')

    while True:
        try:
            recording_duration = float(input("Enter recording duration in seconds: "))
            if recording_duration <= 0:
                raise ValueError("Duration must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    recorder.record_screen(recording_duration)