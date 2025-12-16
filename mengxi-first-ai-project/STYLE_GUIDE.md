# Pregnancy & Parenting Tools - Style Guide

## Overview
This style guide establishes a unified visual language for all pregnancy and parenting web applications, including:
- Contraction Timer
- Feeding Tracker
- Diaper Counter
- Baby Sleep Tracker
- Pregnancy Calculator

## Design Philosophy
A calm, reassuring, and user-friendly interface that aligns with the needs of expectant parents and caregivers.

## Typography

### Font Family
```css
body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}
```
- Uses system fonts for optimal performance and accessibility
- Ensures consistent rendering across all devices

### Font Sizes
| Element               | Font Size |
|-----------------------|-----------|
| Body Text             | 18px      |
| Headings              | 2rem      |
| Timer Display         | 3rem      |
| Stat Values           | 2rem      |
| Stat Labels           | 0.9rem    |
| Button Text           | 18px      |

### Font Weights
- Normal: 400
- Bold: 700 (used for headings, timer displays, and stat values)

## Color Scheme

### Light Mode
```css
:root {
    --pico-primary: #3498db;       /* Calming blue - primary actions */
    --pico-secondary: #F8E1E9;     /* Blush pink - background accents */
    --pico-accent: #80CBC4;        /* Soft teal - secondary highlights */
    --pico-color: #333333;         /* Dark gray - body text */
    --pico-background-color: #F5F5F5; /* Light gray - page background */
    --pico-muted-color: #666666;   /* Medium gray - secondary text */
}
```

### Dark Mode
```css
@media (prefers-color-scheme: dark) {
    :root {
        --pico-background-color: #1A1A2E; /* Dark navy - page background */
        --pico-color: #E8E8E8;            /* Soft white - body text */
        --pico-primary: #FFB74D;          /* Warm amber - primary actions */
    }
}
```

## Interactive Elements

### Buttons & Inputs
- Minimum touch target: 48px height
- Font size: 18px
- Border-radius: 8px (Pico CSS default)

### Cards
- Maximum width: 500px (centered on page)
- Background: White (light mode) / Dark elements (dark mode)
- Border-radius: 8px

### Stats Display
- Grid layout for statistics
- Background: var(--pico-secondary)
- Padding: 1.5rem
- Border-radius: 12px
- Centered text

## Accessibility
- High contrast ratios for text and background
- Large touch targets
- Semantic HTML structure
- Responsive design for all screen sizes

## Consistency Rules
1. All applications must use the same CSS variables defined above
2. All text must be in English
3. Touch targets must be consistent at 48px minimum height
4. Layout structure should follow the card-based design pattern
