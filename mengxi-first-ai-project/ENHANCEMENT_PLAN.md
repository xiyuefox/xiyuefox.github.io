# Sheikah Slate Data Stream Enhancement Plan

## 1. Current Functionality Overview
The current program creates a terminal-based digital rain effect inspired by The Matrix, with the following features:
- Falling streams of random characters (numbers, letters, symbols)
- Cyan color scheme
- Adjustable falling speed per stream
- Exit on 'q' key press

## 2. Enhancement Ideas

### 2.1 Visual Improvements
- **Gradient color effects**: Start with bright cyan at the top of streams, fading to darker blue
- **Character variation**: Add Sheikah-themed symbols (if available) or more contextually appropriate characters
- **Stream length variation**: Different streams have different lengths
- **Background effects**: Subtle grid or glow effects
- **Animation on stream reset**: Smooth entrance/exit animations

### 2.2 Interactive Features
- **Mouse support**: Click to add/remove streams
- **Keyboard shortcuts**:
  - Change speed with arrow keys
  - Change color scheme with number keys
  - Pause/Resume with spacebar
  - Clear screen with 'c'
- **Terminal resizing**: Properly handle terminal window resizing

### 2.3 Performance & Quality of Life
- **Frame rate control**: Consistent FPS regardless of terminal size
- **Memory optimization**: Reduce unnecessary calculations
- **Configuration file**: Allow saving/loading preferences
- **Help menu**: Display available shortcuts on 'h' key press
- **Smooth animations**: Better interpolation for falling characters

### 2.4 Thematic Improvements
- **Sheikah language support**: Integrate actual Sheikah symbols/characters
- **Symbol groups**: Different types of characters (tech symbols, numbers, letters) in separate streams
- **Pattern formation**: Streams occasionally form Sheikah Eye or other patterns
- **Sound effects**: Optional terminal bell sounds on certain events

## 3. Proposed Implementation Plan

After considering various enhancement possibilities, I'll propose a plan that balances implementation complexity with visual impact. We'll focus on:

### Phase 1: Core Visual Enhancements (High Impact, Medium Complexity)
1. **Gradient Color System**
2. **Variable Stream Lengths**
3. **Terminal Resizing Support**

### Phase 2: Interactive Features (Medium Impact, Medium Complexity)
4. **Keyboard Shortcuts**
5. **Help Menu**

### Phase 3: Performance & Polish (Low Impact, Low Complexity)
6. **Frame Rate Optimization**
7. **Configuration File Support**

## 4. Detailed Implementation Plan

Let's break down each enhancement with specific implementation details:

### 4.1 Gradient Color System (Phase 1)
- **Description**: Streams will start with bright cyan at the top, fading to darker blue shades
- **Implementation Steps**:
  1. Initialize multiple color pairs (5-10) with varying brightness
  2. For each character in a stream, use a darker color as we go down the stream
  3. Update the drawing loop to use the appropriate color index based on position
- **Files Modified**: `sheikah.py` (main function)
- **Dependencies**: None (uses existing curses color support)

### 4.2 Variable Stream Lengths (Phase 1)
- **Description**: Each stream will have a random length between 5-20 characters
- **Implementation Steps**:
  1. Add a `length` property to each stream in the initialization
  2. Update the drawing loop to only draw up to `length` characters per stream
  3. Ensure streams don't exceed terminal height
- **Files Modified**: `sheikah.py` (stream initialization and drawing)
- **Dependencies**: None

### 4.3 Terminal Resizing Support (Phase 1)
- **Description**: Program will properly adjust to terminal window size changes
- **Implementation Steps**:
  1. Add a resize handler that:
     - Clears the screen
     - Recomputes terminal dimensions
     - Reinitializes streams if needed
  2. Check for resize events in the main loop
- **Files Modified**: `sheikah.py` (main loop and initialization)
- **Dependencies**: curses `KEY_RESIZE` support

### 4.4 Keyboard Shortcuts (Phase 2)
- **Description**: Add the following keyboard shortcuts:
  - `↑`/`↓`: Increase/decrease overall speed
  - `+`/`-`: Increase/decrease stream length
  - `space`: Pause/Resume
  - `h`: Show help menu
- **Implementation Steps**:
  1. Add global variables for speed and length settings
  2. Update the key handling section to detect these keys
  3. Modify stream properties when keys are pressed
- **Files Modified**: `sheikah.py` (key handling and stream properties)
- **Dependencies**: None

### 4.5 Help Menu (Phase 2)
- **Description**: Show a help screen with available shortcuts when 'h' is pressed
- **Implementation Steps**:
  1. Create a `show_help` function that draws the help screen
  2. Toggle help screen visibility when 'h' is pressed
  3. Ensure help screen is cleared when hidden
- **Files Modified**: `sheikah.py` (add new function)
- **Dependencies**: None

### 4.6 Frame Rate Optimization (Phase 3)
- **Description**: Implement consistent frame rate control
- **Implementation Steps**:
  1. Calculate time per frame based on target FPS (e.g., 60 FPS)
  2. Track elapsed time and sleep only the necessary amount
  3. Avoid unnecessary calculations in the main loop
- **Files Modified**: `sheikah.py` (main loop timing)
- **Dependencies**: None

### 4.7 Configuration File Support (Phase 3)
- **Description**: Allow saving/loading preferences to a JSON file
- **Implementation Steps**:
  1. Create a `config.json` file with default settings
  2. Add functions to load/save configuration
  3. Use loaded settings at program start
- **Files Modified**: `sheikah.py` (add config functions), new `config.json` file
- **Dependencies**: json module (standard library)

## 5. Implementation Timeline Estimate

| Enhancement | Estimated Time |
|-------------|----------------|
| Gradient Color System | 2 hours |
| Variable Stream Lengths | 1 hour |
| Terminal Resizing Support | 1.5 hours |
| Keyboard Shortcuts | 2 hours |
| Help Menu | 1 hour |
| Frame Rate Optimization | 1 hour |
| Configuration File Support | 2 hours |
| **Total** | **10.5 hours** |

## 6. Technical Considerations
- We'll maintain backward compatibility with the original code structure
- All enhancements will be optional (default behavior remains similar)
- We'll use only standard library modules to avoid dependencies
- The code will be well-commented for future maintenance

## 7. Future Expansion Ideas
- Sheikah symbol integration
- Pattern formation algorithms
- Sound effects support
- Multiple color schemes presets

Let me know your thoughts on this plan! If you have specific enhancements you'd like to prioritize or modify, feel free to provide feedback.
