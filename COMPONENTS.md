# Component Documentation

This document provides detailed information about each UI component in the AI Interview Platform.

## Table of Contents
1. [Header](#header)
2. [ProgressStepper](#progressstepper)
3. [InterviewChat](#interviewchat)
4. [ContextPanel](#contextpanel)
5. [FinalEvaluation](#finalevaluation)

---

## Header

**File**: `src/components/Header.jsx`

### Purpose
Displays the application branding and current interview status.

### Props
| Prop | Type | Required | Description |
|------|------|----------|-------------|
| status | string | Yes | Current interview status ("Interview In Progress" or "Interview Completed") |

### Features
- App logo with briefcase icon
- Animated status indicator (pulsing dot for in-progress)
- Responsive layout

### Usage Example
```jsx
<Header status="Interview In Progress" />
```

---

## ProgressStepper

**File**: `src/components/ProgressStepper.jsx`

### Purpose
Visual progress indicator showing all interview rounds and highlighting the current active round.

### Props
| Prop | Type | Required | Description |
|------|------|----------|-------------|
| rounds | Array | Yes | Array of round objects with id, name, and description |
| currentRound | number | Yes | Current active round number (1-3) |

### Features
- Visual stepper with connecting lines
- Checkmark for completed rounds
- Active round highlighting
- Current round description display

### Round Object Structure
```javascript
{
  id: 1,
  name: 'Screening',
  description: 'Behavioral & HR discussion'
}
```

### Usage Example
```jsx
<ProgressStepper 
  rounds={[
    { id: 1, name: 'Screening', description: 'Behavioral & HR' },
    { id: 2, name: 'Technical', description: 'Skills assessment' },
    { id: 3, name: 'Scenario', description: 'Problem solving' }
  ]}
  currentRound={2}
/>
```

---

## InterviewChat

**File**: `src/components/InterviewChat.jsx`

### Purpose
Main chat interface for the interview conversation between AI and candidate.

### Props
| Prop | Type | Required | Description |
|------|------|----------|-------------|
| messages | Array | Yes | Array of message objects |
| currentRound | number | Yes | Current interview round number |
| onSendMessage | Function | Yes | Callback when user sends a message |

### Features
- Chat bubbles with distinct styling for AI vs User
- Auto-scroll to latest message
- Typing indicator animation
- Message timestamps
- Input field with send button

### Message Object Structure
```javascript
{
  id: 1,
  sender: 'ai', // or 'user'
  text: 'Message content',
  timestamp: new Date(),
  round: 1
}
```

### Usage Example
```jsx
<InterviewChat 
  messages={messagesArray}
  currentRound={1}
  onSendMessage={(text) => console.log(text)}
/>
```

---

## ContextPanel

**File**: `src/components/ContextPanel.jsx`

### Purpose
Displays information about the current interview round and provides helpful tips to the candidate.

### Props
| Prop | Type | Required | Description |
|------|------|----------|-------------|
| currentRound | Object | Yes | Current round object with id, name, and description |

### Features
- Round badge display
- Focus area description
- Interview tips list
- Status indicators
- Helpful note section

### Usage Example
```jsx
<ContextPanel 
  currentRound={{
    id: 1,
    name: 'Screening',
    description: 'Behavioral & HR discussion'
  }}
/>
```

---

## FinalEvaluation

**File**: `src/components/FinalEvaluation.jsx`

### Purpose
Displays comprehensive interview evaluation results after interview completion.

### Props
| Prop | Type | Required | Description |
|------|------|----------|-------------|
| evaluation | Object | Yes | Complete evaluation data object |
| onRestart | Function | Yes | Callback to restart interview (demo) |

### Features
- Verdict card (Recommended/Not Recommended)
- Round-wise performance summaries
- Strengths and improvement areas
- Recruiter notes
- Action buttons (restart, download, share)
- Professional report layout

### Evaluation Object Structure
```javascript
{
  roundSummaries: [
    {
      round: 'Round 1: Screening',
      summary: 'Performance description...'
    }
  ],
  strengths: ['Strength 1', 'Strength 2'],
  improvements: ['Area 1', 'Area 2'],
  verdict: 'Recommended',
  overallScore: 'Strong candidate for the position'
}
```

### Usage Example
```jsx
<FinalEvaluation 
  evaluation={evaluationData}
  onRestart={() => console.log('Restart interview')}
/>
```

---

## Styling Guidelines

### Color Classes
- **Primary**: `bg-primary-600`, `text-primary-600`
- **Neutral**: `bg-neutral-50`, `text-neutral-900`
- **Success**: `bg-green-500`, `text-green-700`
- **Warning**: `bg-orange-500`, `text-orange-700`

### Common Patterns
- Card: `bg-white rounded-lg shadow-sm border border-neutral-200 p-6`
- Button: `px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700`
- Badge: `inline-flex items-center px-3 py-1 rounded-full text-sm font-medium`

### Responsive Utilities
- Stack on mobile: `flex flex-col md:flex-row`
- Grid layout: `grid grid-cols-1 lg:grid-cols-3 gap-6`
- Hide on mobile: `hidden md:block`

---

## Best Practices

### Component Structure
1. Import statements
2. JSDoc comment with component description
3. Props destructuring
4. State hooks and refs
5. Effects and handlers
6. Return JSX

### Naming Conventions
- Components: PascalCase (e.g., `InterviewChat`)
- Files: PascalCase matching component name
- Props: camelCase (e.g., `currentRound`)
- Handlers: `handle` prefix (e.g., `handleSendMessage`)

### Accessibility
- Use semantic HTML elements
- Add ARIA labels where needed
- Ensure keyboard navigation works
- Maintain color contrast ratios

---

**Last Updated**: February 2026
