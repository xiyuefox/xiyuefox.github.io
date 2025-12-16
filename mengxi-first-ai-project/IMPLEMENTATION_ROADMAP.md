# Sheikah Slate Data Stream Implementation Roadmap

## Current Status Analysis

After examining the current `sheikah.py` implementation and the enhancement plans, I've identified which features are already implemented versus planned:

### ✅ Already Implemented Features
1. **Gradient Color System** (Phase 1) - Line 23-27, 73-74
2. **Variable Stream Lengths** (Phase 1) - Line 43
3. **Basic Keyboard Controls** (Phase 2) - Exit on 'q'

### 📋 Planned Features to Implement
1. **Terminal Resizing Support** (Phase 1)
2. **Keyboard Shortcuts** (Phase 2) - arrow keys, spacebar
3. **Help Menu** (Phase 2)
4. **Frame Rate Optimization** (Phase 3)
5. **Configuration File Support** (Phase 3)

## Implementation Roadmap

### Phase 1: Core Visual Enhancements & Stability
**Goal**: Ensure the program handles dynamic terminal environments properly

#### 1. Terminal Resizing Support (High Priority)
**Description**: Handle terminal window resizing gracefully by recalculating dimensions and reinitializing streams.
**Complexity**: Low
**Dependencies**: curses KEY_RESIZE event
**Code Changes**:
- Line 48-50: Add KEY_RESIZE handling
- Main loop: Clear screen and reset streams on resize
- Update height/width variables dynamically

**Implementation Details**:
```python
# In the main loop's key handling section:
elif key == curses.KEY_RESIZE:
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
```

---

### Phase 2: Interactive Features
**Goal**: Make the program more user-friendly and interactive

#### 2. Keyboard Shortcuts (Medium Priority)
**Description**: Implement arrow keys for speed control and spacebar for pause/resume.
**Complexity**: Medium
**Dependencies**: None
**Code Changes**:
- Add global speed_multiplier and paused variables
- Line 48-50: Add handling for up/down arrows and spacebar
- Update stream speed calculations to use multiplier

**Implementation Details**:
```python
# At the beginning of main function:
speed_multiplier = 1.0
paused = False

# In key handling section:
elif key == curses.KEY_UP:
    speed_multiplier *= 0.9  # Increase speed
elif key == curses.KEY_DOWN:
    speed_multiplier *= 1.1  # Decrease speed
elif key == ord(' '):
    paused = not paused

# In stream update section:
if not paused and time.time() - stream['last_update'] > stream['speed'] * speed_multiplier:
    # Update stream logic...
```

#### 3. Help Menu (Medium Priority)
**Description**: Display a help screen with available shortcuts when 'h' is pressed.
**Complexity**: Medium
**Dependencies**: None
**Code Changes**:
- Create `draw_help` function
- Add show_help toggle in key handling
- Display help screen when toggle is active

**Implementation Details**:
```python
# Add this function inside main() or as a helper
def draw_help(stdscr, height, width):
    help_text = [
        "Sheikah Slate Data Stream Help",
        "================================",
        "q: Quit the program",
        "h: Toggle help menu",
        "space: Pause/Resume",
        "↑: Increase speed",
        "↓: Decrease speed",
        "",
        "Press any key to continue..."
    ]
    for i, line in enumerate(help_text):
        if 5 + i < height:
            x = width // 2 - len(line) // 2
            stdscr.addstr(5 + i, x, line, curses.A_BOLD)

# In main loop:
if show_help:
    draw_help(stdscr, height, width)
    stdscr.refresh()
    # Wait for user input
    key = stdscr.getch()
    if key != -1:
        show_help = False
        continue
```

---

### Phase 3: Performance & Quality of Life
**Goal**: Improve overall program performance and user experience

#### 4. Frame Rate Optimization (Low Priority)
**Description**: Implement consistent frame rate control to avoid unnecessary CPU usage.
**Complexity**: Low
**Dependencies**: None
**Code Changes**:
- Replace fixed sleep with dynamic sleep based on target FPS
- Calculate elapsed time per frame

**Implementation Details**:
```python
# At the beginning of main:
target_fps = 60
frame_time = 1.0 / target_fps

# In main loop:
start_time = time.time()

# Main loop logic...

# Control frame rate
elapsed = time.time() - start_time
if elapsed < frame_time:
    time.sleep(frame_time - elapsed)
```

#### 5. Configuration File Support (Low Priority)
**Description**: Allow loading/saving preferences from a JSON configuration file.
**Complexity**: Medium
**Dependencies**: json module (standard library)
**Code Changes**:
- Add json import
- Create default configuration
- Load config file on startup
- Use config values in initialization

**Implementation Details**:
```python
import json

# Default configuration
DEFAULT_CONFIG = {
    "target_fps": 60,
    "min_stream_length": 5,
    "max_stream_length": 20,
    "min_speed": 0.05,
    "max_speed": 0.3,
    "speed_multiplier": 1.0
}

# Load configuration
def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return DEFAULT_CONFIG

# In main function:
config = load_config()
target_fps = config['target_fps']
```

## Implementation Order & Dependencies

```
1. Terminal Resizing Support ───┐
2. Keyboard Shortcuts ───┐      │
3. Help Menu ────────────┼──────┼──> 4. Frame Rate Optimization
                          │      │
                          └──────┼──> 5. Configuration File Support
                                 │
                                 └──> 5. Configuration File Support
```

**Task Dependencies**:
- Frame Rate Optimization can be implemented independently
- Configuration File Support depends on Keyboard Shortcuts and Frame Rate Optimization for configurable values

## Testing Strategy

For each enhancement:
1. Test basic functionality (e.g., resizing works, shortcuts respond)
2. Test edge cases (very small/large terminal, rapid resizing)
3. Test backward compatibility (ensure 'q' still exits)
4. Test performance (CPU usage, smoothness)

## Backward Compatibility

All enhancements will maintain backward compatibility:
- Default behavior remains unchanged
- Existing 'q' key exit still works
- Original code structure is preserved
- No external dependencies are added

## Estimated Timeline

| Enhancement | Estimated Time |
|-------------|----------------|
| Terminal Resizing Support | 1 hour |
| Keyboard Shortcuts | 2 hours |
| Help Menu | 1.5 hours |
| Frame Rate Optimization | 1 hour |
| Configuration File Support | 2.5 hours |
| **Total** | **8 hours** |

This roadmap provides a clear, structured path to implement all planned enhancements while maintaining quality, performance, and backward compatibility.
