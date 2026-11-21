import os
import signal
import time
from pathlib import Path

LED = Path("/sys/class/leds") / os.environ.get("BLINK_LED", "ACT")
stop = False


def request_stop(signum, frame):
    global stop
    stop = True


def write(path: Path, text: str) -> None:
    path.write_text(text)


def main() -> None:
    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)
    trigger = LED / "trigger"
    brightness = LED / "brightness"
    if not trigger.is_file():
        raise SystemExit(f"The onboard LED is not available at {LED}")
    write(trigger, "none")
    state = 0
    try:
        while not stop:
            state = 0 if state else 1
            write(brightness, str(state))
            time.sleep(1)
    finally:
        write(trigger, "mmc0")


if __name__ == "__main__":
    main()
