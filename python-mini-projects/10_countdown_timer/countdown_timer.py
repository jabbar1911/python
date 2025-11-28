#!/usr/bin/env python3
"""Countdown Timer - Improved Version"""

import time
import sys

# Color codes
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def format_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60

    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"

def countdown(total):
    print(f"\n{CYAN}Timer started... Press Ctrl+C to stop{RESET}\n")

    try:
        for remain in range(total, -1, -1):
            t = format_time(remain)

            # Progress bar (30 blocks for smooth effect)
            filled = int(((total - remain) / total) * 30) if total > 0 else 30
            bar = GREEN + "█" * filled + RESET + "░" * (30 - filled)

            sys.stdout.write(f"\r⏱️  {YELLOW}{t}{RESET}  [{bar}]")
            sys.stdout.flush()

            time.sleep(1)

        # final output
        print("\n\n⏰ TIME'S UP! ⏰\n")
        for _ in range(3):
            print('\a', end='', flush=True)
            time.sleep(0.4)

    except KeyboardInterrupt:
        print(f"\n\n⏹ Timer Stopped! Remaining: {format_time(remain)}")

def parse_time(s):
    if ":" not in s:
        return int(s)

    parts = list(map(int, s.split(":")))
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    elif len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    else:
        raise ValueError

def main():
    print("=" * 60)
    print("COUNTDOWN TIMER".center(60))
    print("=" * 60)

    while True:
        print("\nFormats:  90  (seconds)")
        print("          5:30  (MM:SS)")
        print("          1:30:00 (HH:MM:SS)")

        t = input("\nEnter time: ").strip()

        try:
            total = parse_time(t)
            if total > 0:
                countdown(total)
                break
        except:
            print("❌ Invalid time format!")

if __name__ == "__main__":
    main()
