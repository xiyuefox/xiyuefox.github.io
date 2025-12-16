#!/usr/bin/env python3
"""
Sheikah Slate Data Stream - Inspired by The Matrix Digital Rain
"""

import curses
import random
import time

def main(stdscr):
    # Initialize curses
    curses.noecho()
    curses.curs_set(0)
    stdscr.nodelay(1)
    curses.start_color()

    # Initialize color pairs for gradient (bright to dark)
    # 1: Bright cyan (head)
    # 2: Blue
    # 3: Dark blue
    # 4: Darker blue
    # 5: Darkest blue (tail)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Bright cyan
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)     # Blue
    curses.init_pair(3, 24, curses.COLOR_BLACK)                   # Dark blue (ANSI 24)
    curses.init_pair(4, 23, curses.COLOR_BLACK)                   # Darker blue (ANSI 23)
    curses.init_pair(5, 17, curses.COLOR_BLACK)                   # Darkest blue (ANSI 17 - navy)

    # Get terminal dimensions
    height, width = stdscr.getmaxyx()

    # Characters to use in the stream
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ△▲✦✧★"

    # Initialize global variables for controls
    speed_multiplier = 1.0
    paused = False

    # Initialize falling streams
    streams = []
    for i in range(width):
        # Random starting position, speed, and length
        streams.append({
            'pos': random.randint(-height * 2, 0),
            'speed': random.uniform(0.05, 0.3),
            'last_update': time.time(),
            'length': random.randint(5, 20)  # Variable stream length
        })

    while True:
        # Check for exit key (q)
        key = stdscr.getch()
        if key == ord('q'):
            break

        # Handle terminal resize
        if key == curses.KEY_RESIZE:
            # Clear screen and get new dimensions
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            # Reinitialize streams with new width
            streams = []
            for i in range(width):
                streams.append({
                    'pos': random.randint(-height * 2, 0),
                    'speed': random.uniform(0.05, 0.3),
                    'last_update': time.time(),
                    'length': random.randint(5, 20)
                })

        # Handle keyboard shortcuts
        elif key == curses.KEY_UP:
            # Increase speed
            speed_multiplier *= 0.9
        elif key == curses.KEY_DOWN:
            # Decrease speed
            speed_multiplier *= 1.1
        elif key == ord(' '):
            # Toggle pause
            paused = not paused

        # Clear screen
        stdscr.clear()

        # Update each stream
        for i, stream in enumerate(streams):
            if not paused and time.time() - stream['last_update'] > stream['speed'] * speed_multiplier:
                # Move stream down
                stream['pos'] += 1
                stream['last_update'] = time.time()

                # Reset stream when it goes off screen
                if stream['pos'] > height:
                    stream['pos'] = random.randint(-height, 0)
                    stream['speed'] = random.uniform(0.05, 0.3)

            # Draw stream with gradient
            for j in range(stream['length']):
                char_pos = stream['pos'] - j
                if 0 <= char_pos < height:
                    char = random.choice(chars)
                    # Calculate color index: brightest at head (1), darker towards tail
                    color_idx = min(5, j // 2 + 1)  # 1=bright cyan, 5=darkest blue
                    stdscr.addstr(char_pos, i, char, curses.color_pair(color_idx))

        # Refresh screen
        stdscr.refresh()

        # Control frame rate
        time.sleep(0.01)

if __name__ == "__main__":
    curses.wrapper(main)
