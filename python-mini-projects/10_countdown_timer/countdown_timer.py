#!/usr/bin/env python3
"""Countdown Timer"""

import time
import sys

def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60

    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"

def countdown(total):
    remaining = total

    print("Timer started... Press Ctrl+C to stop\n")

    try:
        while remaining > 0:
            time_str = format_time(remaining)
            progress = (total - remaining) / total * 20
            bar = '█' * int(progress) + '░' * (20 - int(progress))

            sys.stdout.write(f'\r⏱️  {time_str} [{bar}]')
            sys.stdout.flush()

            time.sleep(1)
            remaining -= 1

        sys.stdout.write('\r')
        print("⏰ TIME'S UP! ⏰\n")
        for _ in range(3):
            print('\a', end='', flush=True)
            time.sleep(0.5)

    except KeyboardInterrupt:
        print(f"\nStopped! Remaining: {format_time(remaining)}")

def main():
    print("=" * 60)
    print("COUNTDOWN TIMER".center(60))
    print("=" * 60)

    while True:
        print("\nFormats: 90 (seconds), 5:30 (MM:SS), 1:30:00 (HH:MM:SS)")
        time_input = input("Enter time: ").strip()

        try:
            if ':' in time_input:
                parts = list(map(int, time_input.split(':')))
                if len(parts) == 2:
                    total = parts[0] * 60 + parts[1]
                elif len(parts) == 3:
                    total = parts[0] * 3600 + parts[1] * 60 + parts[2]
                else:
                    print("Invalid format!")
                    continue
            else:
                total = int(time_input)

            if total > 0:
                countdown(total)
                break
        except:
            print("Invalid input!")

if __name__ == "__main__":
    main()
