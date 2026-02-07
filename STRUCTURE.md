# Project File Structure

## Complete Directory Tree

```
Creeper-code-a-thon/
│
├── src/
│   ├── pages/
│   │   ├── HomePage.jsx               # Landing page with start button (~130 lines)
│   │   ├── RoundPage.jsx              # Shared round page for all 3 rounds (~200 lines)
│   │   └── EvaluationPage.jsx         # Final evaluation page (~60 lines)
│   │
│   ├── components/
│   │   ├── Header.jsx                 # Top navigation bar with status
│   │   ├── ProgressStepper.jsx        # Visual round progress tracker
│   │   ├── InterviewChat.jsx          # Main chat conversation interface
│   │   ├── ContextPanel.jsx           # Round info and tips sidebar
│   │   └── FinalEvaluation.jsx        # Post-interview results view
│   │
│   ├── App.jsx                        # Main app with React Router (~35 lines)
│   ├── main.jsx                       # React app entry point
│   └── index.css                      # Global styles & Tailwind imports
│
├── index.html                         # HTML template
├── package.json                       # Dependencies & scripts
├── vite.config.js                     # Vite bundler configuration
├── tailwind.config.js                 # Tailwind CSS configuration
├── postcss.config.js                  # PostCSS configuration
├── .gitignore                         # Git ignore rules
│
├── README.md                          # Main project documentation
├── SETUP.md                           # Quick setup guide
├── COMPONENTS.md                      # Component API documentation
├── DESIGN.md                          # Design system documentation
├── ROUTING.md                         # Routing & navigation guide
└── STRUCTURE.md                       # This file
```

---

## File Roles & Responsibilities

### Configuration Files

| File | Purpose | When to Edit |
|------|---------|--------------|
| `package.json` | NPM dependencies, scripts | Adding new packages |
| `vite.config.js` | Dev server, build settings | Changing port, plugins |
| `tailwind.config.js` | Theme colors, fonts, spacing | Customizing design |
| `postcss.config.js` | CSS processing | Rarely needed |
| `.gitignore` | Files to exclude from Git | Adding new ignore patterns |

### Source Code Files

| File | Lines (approx) | Purpose |
|------|----------------|---------|
| `src/main.jsx` | ~10 | React initialization |
| `src/index.css` | ~40 | Global styles, Tailwind imports |
| `src/App.jsx` | ~35 | Main app with React Router routing |
| `src/pages/HomePage.jsx` | ~130 | Landing page component |
| `src/pages/RoundPage.jsx` | ~200 | Shared round page (handles rounds 1-3) |
| `src/pages/EvaluationPage.jsx` | ~60 | Final evaluation page |
| `src/components/Header.jsx` | ~40 | Header component |
| `src/components/ProgressStepper.jsx` | ~80 | Progress stepper component |
| `src/components/InterviewChat.jsx` | ~150 | Chat interface component |
| `src/components/ContextPanel.jsx` | ~80 | Context panel component |
| `src/components/FinalEvaluation.jsx` | ~200 | Evaluation report component |

### Documentation Files

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Project overview, features, setup | Everyone |
| `SETUP.md` | Quick start guide | First-time users |
| `COMPONENTS.md` | Component API reference | Developers |
| `DESIGN.md` | Design system guide | Designers/Developers |
| `ROUTING.md` | Navigation & routing guide | Developers |
| `STRUCTURE.md` | File organization reference | Developers |

---

## Component Hierarchy

``` with Router)
│
├── Router
│   │
│   ├── Route: "/" → HomePage
│   │   └── HomePage
│   │       ├── Welcome section
│   │       ├── Interview structure overview
│   │       └── Start Interview button
│   │
│   ├── Route: "/round/:roundId" → RoundPage
│   │   └── RoundPage (Dynamic - handles round 1, 2, 3)
│   │       ├── Header (status: "In Progress")
│   │       ├── ProgressStepper (current round highlighted)
│   │       ├── InterviewChat (2/3 width)
│   │       │   ├── Chat header
│   │       │   ├── Messages container
│   │       │   │   ├── AI messages (left)
│   │       │   │   ├── User messages (right)
│   │       │   │   └── Typing indicator
│   │       │   └── Input form
│   │       └── ContextPanel (1/3 width)
│   │           ├── Round information
│   │           ├── Tips
│   │           └── Demo controls
│   │
│   ├── Route: "/evaluation" → EvaluationPage
│   │   └── EvaluationPage
│   │       ├── Header (status: "Completed")
│   │       └── FinalEvaluation
│   │           ├── Verdict card
│   │           ├── Round summaries
│   │           ├── Strengths/Improvements
│   │           └── Action buttons
│   │
│   └── Route: "*" → Navigate to "/"ovements
    └── Action buttons
```Routing Only - No State)
│
└── React Router manages URL state
    │
    ├── HomePage (/):
    │   └── No state - just navigation
    │
    ├── RoundPage (/round/:roundId):
    │   ├── Local State:
    │   │   ├── messages: Array<Message>
    │   │   ├── messageCounter: number
    │   │   └── currentRound: number (from URL param)
    │   │
    │   └── Props passed to children:
    │       ├── Header ← status
    │       ├── ProgressStepper ← rounds, currentRound
    │       ├── InterviewChat ← messages, currentRound, onSendMessage
    │       └── ContextPanel ← currentRound
    │
    └── EvaluationPage (/evaluation):
        ├── Static evaluation data
        └── Props passed to:
            └── FinalEvaluation ← evaluationData, onRestart
└── evaluationData: Object
    │
    ├── Passed to Header → status
    ├── Passed to ProgressStepper → currentRound
    ├── Passed to InterviewChat → messages, currentRound
    ├── Passed to ContextPanel → currentRound
    └── Passed to FinalEvaluation → evaluationData
```

---

## Data Models

### Message Object
```typescript
{
  id: number,
  sender: 'ai' | 'user',
  text: string,
  timestamp: Date,
  round: number
}
```

### Round Object
```typescript
{
  id: number,
  name: string,
  description: string
}
```

### Evaluation Object
```typescript
{
  roundSummaries: Array<{
    round: string,
   react-router-dom": "^6.21.0",   // Routing library
  " summary: string
  }>,
  strengths: Array<string>,
  improvements: Array<string>,
  verdict: 'Recommended' | 'Not Recommended',
  overallScore: string
}
```

---

## Key Dependencies

### Production
```json
{
  "react": "^18.2.0",              // UI library
  "react-dom": "^18.2.0",          // React DOM renderer
  "lucide-react": "^0.294.0"       // Icon library
}
```

### Development
```json
{
  "@vitejs/plugin-react": "^4.2.1",  // Vite React support
  "autoprefixer": "^10.4.16",         // PostCSS plugin
  "postcss": "^8.4.32",               // CSS processor
  "tailwindcss": "^3.3.6",            // Utility CSS framework
  "vite": "^5.0.8"                    // Build tool
}
```

---

## Build Process

### Development Mode
```
npm run dev
    ↓
Vite starts dev server
    ↓
Watches files for changes
    ↓
Hot Module Replacement (HMR)
    ↓
Instant browser updates
```

### Production Build
```
npm run build
    ↓
Vite builds optimized bundle
    ↓
- Minifies JavaScript
- Optimizes CSS
- Processes Tailwind
- Creates source maps
    ↓
OutpuNavigate the App**
   - Home page loads at `/`
   - Click "Start Interview" → `/round/1`
   - Progress through rounds → `/round/2`, `/round/3`
   - Complete interview → `/evaluation`

3. **Make Changes**
   - Edit page files in `src/pages/`
   - Edit component files in `src/components/`
   - Changes auto-refresh in browser

4. **Test Navigation**
   - Click buttons to test routing
   - Manually type URLs to test direct access
   - Check back button behavior

5. **Build for Production**
   ```bash
   npm run build
   ```

6  - Changes auto-refresh in browser

3. **Test Features**
   - Interact with UI
   - Check console for errors
   - Test responsive design
Page/Component Props)
- **Round Names**: [src/pages/RoundPage.jsx](src/pages/RoundPage.jsx) - `rounds` array
- **AI Responses**: [src/pages/RoundPage.jsx](src/pages/RoundPage.jsx) - `getAIResponse` function
- **Evaluation Data**: [src/pages/EvaluationPage.jsx](src/pages/EvaluationPage.jsx) - `evaluationData` object
- **Home Page Content**: [src/pages/HomePage.jsx](src/pages/HomePage.jsx) - Text and structure

### Advanced Customizations (Component Logic & Routing)
- **New Routes**: Add to [src/App.jsx](src/App.jsx)
- **New Pages**: Create in `src/pages/`
- **New Components**: Create in `src/components/`
- **State Management**: Modify page components or add Context API

---

## Customization Points

### Easy Customizations (No Component Changes)
- **Colors**: [tailwind.config.js](tailwind.config.js)
- **Fonts**: [tailwind.config.js](tailwind.config.js) + [index.html](index.html)
- **Port**: [vite.config.js](vite.config.js)

### Medium Customizations (Component Props)
- **Round Names**: [src/App.jsx](src/App.jsx) - `rounds` array
- **AI Responses**: [src/App.jsx](src/App.jsx) - `getAIResponse` function
- **Evaluation Data**: [src/App.jsx](src/App.jsx) - `evaluationData` object
to Round Pages

1. **Create Component**
   ```bash
   # Create src/components/Timer.jsx
   ```

2. **Import in RoundPage**
   ```javascript
   import Timer from '../components/Timer';
   ```

3. **Add to Layout**
   ```jsx
   <Timer duration={1800} />
   ```

4. **Style with Tailwind**
   ```jsx
   <div className="bg-white rounded-lg p-4">
     {/* Timer content */}
   </div>
   ```

### Example: Add a New Route

1. **Create Page Component**
   ```bash
   # Create src/pages/HelpPage.jsx
   ```
Add new route | `src/App.jsx` | 18-22 |
| Change home page content | `src/pages/HomePage.jsx` | Throughout |
| Add interview round | `src/pages/RoundPage.jsx` | 17-42 |
| Modify AI response | `src/pages/RoundPage.jsx` | 100-130 |
| Change primary color | `tailwind.config.js` | 12-22 |
| Edit evaluation criteria | `src/pages/EvaluationPage.jsx` | 14-40
   <Route path="/help" element={<HelpPage />} />
   ```

3. **Navigate to Route**
   ```javascript
   navigate('/help');
3. **Add to Layout**
   ```jsx
   <Timer duration={1800} />
   ```

4. **Style with Tailwind**
   ```jsx
   <div className="bg-white rounded-lg p-4">
     {/* Timer content */}
   </div>
   ```

---

## Common Tasks Reference

| Task | File to Edit | Line(s) |
|------|-------------|---------|
| Change app name | `src/components/Header.jsx` | 16 |
| Add interview round | `src/App.jsx` | 15-19 |
| Modify AI response | `src/App.jsx` | 64-80 |
| Change primary color | `tailwind.config.js` | 12-22 |
| Edit evaluation criteria | `src/App.jsx` | 24-45 |
| Update interview tips | `src/components/ContextPanel.jsx` | 32-46 |

---

## Troubleshooting Guide

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| Blank page | Build error | Check browser console |
| Styles broken | Tailwind not loading | Run `npm install` |
| Changes not showing | Cache issue | Hard refresh (Ctrl+Shift+R) |
| Icons missing | lucide-react not installed | `npm install lucide-react` |
| Port in use | 3000 already taken | Vite will auto-select next port |

---

## Performance Considerations

### Optimizations Applied
- ✅ Component code splitting ready
- ✅ CSS purged in production build
- ✅ React StrictMode enabled
- ✅ Efficient re-renders with proper state management

### Future Optimizations
- [ ] Implement React.memo for expensive components
- [ ] Add lazy loading for routes
- [ ] Virtualize long message lists
- [ ] Optimize image assets

---

## Security Considerations

### Current Status
- ✅ No user authentication required
- ✅ No sensitive data stored
- ✅ Client-side only application
- ⚠️ Input validation needed for production

### Before Production
- [ ] Add input sanitization
- [ ] Implement rate limiting
- [ ] Add HTTPS enforcement
- [ ] Configure CSP headers

---

**File Structure Version**: 1.0  
**Last Updated**: February 2026
