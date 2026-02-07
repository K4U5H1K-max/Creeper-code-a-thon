# Design System - AI Interview Platform

## 🎨 Visual Design Language

### Design Philosophy
The AI Interview Platform follows a **professional, calm, and trustworthy** design approach suitable for enterprise recruitment contexts. The interface prioritizes clarity, readability, and a stress-free experience for candidates.

---

## Color System

### Primary Palette

#### Primary Blue (Brand & Interactive Elements)
```
primary-50:  #eff6ff  (Lightest - backgrounds)
primary-100: #dbeafe  (Subtle highlights)
primary-200: #bfdbfe  (Hover backgrounds)
primary-300: #93c5fd  (Light accents)
primary-400: #60a5fa  (Medium accents)
primary-500: #3b82f6  (Base primary color)
primary-600: #2563eb  (Primary buttons, active states) ⭐ Main
primary-700: #1d4ed8  (Hover states, emphasis)
primary-800: #1e40af  (Deep emphasis)
primary-900: #1e3a8a  (Darkest)
```

**Usage**: 
- Call-to-action buttons
- Active round indicators
- Links and interactive elements
- AI message highlights

#### Neutral Grays (Backgrounds & Text)
```
neutral-50:  #fafafa  (Page background) ⭐ Main background
neutral-100: #f5f5f5  (Card backgrounds, subtle areas)
neutral-200: #e5e5e5  (Borders, dividers)
neutral-300: #d4d4d4  (Light borders)
neutral-400: #a3a3a3  (Disabled text)
neutral-500: #737373  (Secondary text)
neutral-600: #525252  (Body text)
neutral-700: #404040  (Emphasis text)
neutral-800: #262626  (Headings)
neutral-900: #171717  (Primary text) ⭐ Main text
```

**Usage**:
- Page and card backgrounds
- Text hierarchy
- Borders and dividers
- Disabled states

### Semantic Colors

#### Success Green
```
green-50:  #f0fdf4  (Success message backgrounds)
green-100: #dcfce7  (Success badges)
green-500: #22c55e  (Completed indicators)
green-600: #16a34a  (Success buttons)
green-700: #15803d  (Success emphasis)
```

**Usage**:
- Completed rounds
- Positive recommendations
- Success states

#### Warning Orange
```
orange-50:  #fff7ed  (Warning backgrounds)
orange-100: #ffedd5  (Warning highlights)
orange-500: #f97316  (Warning indicators)
orange-600: #ea580c  (Warning emphasis)
```

**Usage**:
- Areas for improvement
- Caution states

#### Error Red
```
red-50:  #fef2f2  (Error backgrounds)
red-100: #fee2e2  (Error highlights)
red-500: #ef4444  (Error states)
red-600: #dc2626  (Error emphasis)
red-700: #b91c1c  (Critical errors)
```

**Usage**:
- Negative recommendations
- Error states

#### Info Blue
```
blue-50:  #eff6ff  (Info backgrounds)
blue-100: #dbeafe  (Info highlights)
blue-800: #1e40af  (Info text)
```

**Usage**:
- Informational notes
- Helper text areas

---

## Typography

### Font Family
```css
font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 
             'Segoe UI', 'Roboto', sans-serif;
```

**Rationale**: Inter is a professional, highly readable sans-serif font designed specifically for digital interfaces. It maintains clarity at all sizes.

### Type Scale

#### Headings
```css
/* Main Title - H1 */
text-3xl (1.875rem / 30px) - font-bold
Usage: Page titles, main headings

/* Section Title - H2 */
text-xl (1.25rem / 20px) - font-semibold
Usage: Section headings, card titles

/* Subsection Title - H3 */
text-lg (1.125rem / 18px) - font-semibold
Usage: Subsection headings

/* Small Heading - H4 */
text-sm (0.875rem / 14px) - font-semibold
Usage: Card subtitles, labels
```

#### Body Text
```css
/* Regular Body */
text-sm (0.875rem / 14px) - font-normal
Usage: Main body content, messages

/* Small Text */
text-xs (0.75rem / 12px) - font-normal
Usage: Timestamps, helper text, captions
```

### Font Weights
- **Light (300)**: Subtle text, decorative
- **Regular (400)**: Body text, descriptions
- **Medium (500)**: Emphasized text
- **Semibold (600)**: Headings, labels ⭐ Most common for headings
- **Bold (700)**: Strong emphasis, titles

### Line Heights
```css
leading-tight: 1.25     (Headings)
leading-relaxed: 1.625  (Body text, chat messages)
leading-loose: 2        (Spacious content)
```

---

## Spacing System

### Base Unit: 4px
All spacing uses multiples of 4px for visual consistency.

```
spacing-1:  4px   (0.25rem)
spacing-2:  8px   (0.5rem)  - Tight spacing
spacing-3:  12px  (0.75rem) - Close elements
spacing-4:  16px  (1rem)    - Default gap
spacing-6:  24px  (1.5rem)  - Card padding ⭐ Standard
spacing-8:  32px  (2rem)    - Section spacing
spacing-12: 48px  (3rem)    - Large sections
spacing-16: 64px  (4rem)    - Major sections
```

### Component Spacing Guidelines
- **Card Padding**: `p-6` (24px)
- **Element Gaps**: `gap-6` (24px) or `gap-4` (16px)
- **Section Margins**: `mb-6` (24px)
- **Button Padding**: `px-6 py-3` (24px horizontal, 12px vertical)

---

## Component Patterns

### Cards
```css
/* Standard Card */
bg-white rounded-lg shadow-sm border border-neutral-200 p-6

/* Emphasized Card */
bg-white rounded-lg shadow-md border-2 border-primary-600 p-6

/* INFO Card */
bg-blue-50 rounded-lg border border-blue-200 p-6
```

### Buttons

#### Primary Button
```css
px-6 py-3 bg-primary-600 text-white rounded-lg 
hover:bg-primary-700 transition-colors font-medium
```

#### Secondary Button
```css
px-6 py-3 bg-white text-neutral-700 border-2 border-neutral-300 
rounded-lg hover:bg-neutral-50 transition-colors font-medium
```

#### Success Button
```css
px-6 py-3 bg-green-600 text-white rounded-lg 
hover:bg-green-700 transition-colors font-medium
```

### Badges
```css
/* Status Badge */
inline-flex items-center px-3 py-1 rounded-full 
text-sm font-medium bg-primary-100 text-primary-700

/* Success Badge */
inline-flex items-center px-3 py-1 rounded-full 
text-sm font-medium bg-green-100 text-green-700
```

### Input Fields
```css
px-4 py-3 border border-neutral-300 rounded-lg 
focus:outline-none focus:ring-2 focus:ring-primary-500 
focus:border-transparent bg-white
```

---

## Shadows

### Elevation System
```css
shadow-sm:  0 1px 2px rgba(0,0,0,0.05)    - Subtle lift (cards)
shadow:     0 1px 3px rgba(0,0,0,0.1)     - Default elevation
shadow-md:  0 4px 6px rgba(0,0,0,0.1)     - Medium elevation
shadow-lg:  0 10px 15px rgba(0,0,0,0.1)   - High elevation (modals)
```

**Usage Guidelines**:
- Cards: `shadow-sm`
- Hover states: `shadow-md`
- Modals/dropdowns: `shadow-lg`

---

## Border Radius

```css
rounded:     4px   (0.25rem) - Subtle corners
rounded-lg:  8px   (0.5rem)  - Standard (cards, buttons) ⭐
rounded-full: 50%            - Circles (avatars, badges)
```

---

## Icons

### Icon Library
**Lucide React** - Consistent, professional icon set

### Icon Sizes
```css
w-4 h-4:  16px  - Small (inline with text)
w-5 h-5:  20px  - Medium (buttons, labels) ⭐ Standard
w-6 h-6:  24px  - Large (headers, emphasis)
w-8 h-8:  32px  - Extra large (feature highlights)
w-12 h-12: 48px - Hero icons
```

### Icon Usage
- Always pair with text labels for clarity
- Use consistent sizes within component groups
- Apply appropriate colors matching context

---

## Layout Grid

### Responsive Breakpoints
```css
sm:  640px   (Tablet portrait)
md:  768px   (Tablet landscape)
lg:  1024px  (Desktop) ⭐ Primary breakpoint
xl:  1280px  (Large desktop)
2xl: 1536px  (Extra large)
```

### Container
```css
max-w-7xl mx-auto px-4 sm:px-6 lg:px-8
```

### Grid Layouts
```css
/* Main Dashboard Layout (Desktop) */
grid grid-cols-1 lg:grid-cols-3 gap-6

/* Two Column Layout */
grid grid-cols-1 md:grid-cols-2 gap-6
```

---

## Animation & Transitions

### Transition Timing
```css
transition-colors duration-200    - Color changes
transition-all duration-300       - Multiple properties
```

### Animation Classes
```css
animate-pulse     - Pulsing dot (status indicator)
animate-bounce    - Typing indicator dots
```

### Hover Effects
- Buttons: Darken color by one shade
- Cards: Slight shadow increase
- Links: Underline appearance

---

## Accessibility

### Color Contrast
- All text meets WCAG AA standards (4.5:1 for normal text)
- Primary blue (#2563eb) on white: 7.4:1 ✓
- Neutral-900 (#171717) on white: 16.1:1 ✓

### Focus States
```css
focus:outline-none focus:ring-2 focus:ring-primary-500 
focus:ring-offset-2
```

### Touch Targets
- Minimum 44x44px for all interactive elements
- Buttons: 48px minimum height
- Form inputs: 48px minimum height

---

## Best Practices

### Do's ✅
- Use consistent spacing from the 4px grid
- Apply shadow-sm to cards for subtle depth
- Use semantic colors (green for success, red for errors)
- Maintain ample white space
- Keep text hierarchy clear with size/weight
- Use transition-colors for smooth interactions

### Don'ts ❌
- Don't use arbitrary spacing values
- Don't mix too many colors in one view
- Don't create tiny touch targets (<44px)
- Don't use pure black (#000000)
- Don't forget hover/focus states
- Don't overuse animations

---

## Component-Specific Design Notes

### Header
- Fixed height: 64px (h-16)
- White background with subtle bottom border
- Logo size: 24px (w-6 h-6)

### Progress Stepper
- Step circles: 48px (w-12 h-12)
- Connecting line: 2px height
- Completed: green-500
- Active: primary-600
- Inactive: neutral-300

### Chat Messages
- AI messages: Left-aligned, neutral-100 background
- User messages: Right-aligned, primary-600 background
- Avatar size: 40px (w-10 h-10)
- Max message width: 80%

### Chat Container
- Fixed height: 600px
- Scrollable message area
- Input area: Fixed at bottom

### Context Panel
- Sticky positioning on desktop
- Full width on mobile
- Background: white card

### Final Evaluation
- Maximum width: 80rem (1280px)
- Centered layout
- Generous spacing between sections

---

## Responsive Design Strategy

### Mobile First Approach
1. Design for mobile (320px+)
2. Enhance for tablet (640px+)
3. Optimize for desktop (1024px+)

### Key Responsive Changes
- Stack columns on mobile
- Reduce padding on small screens
- Adjust font sizes for readability
- Simplify navigation

---

**Design System Version**: 1.0  
**Last Updated**: February 2026  
**Maintained by**: Creeper Code-a-thon Team
