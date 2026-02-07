# Routing & Navigation Guide

## 📍 Route Structure

The AI Interview Platform uses React Router DOM v6 for client-side routing and navigation.

### Route Map

| Route | Component | Purpose |
|-------|-----------|---------|
| `/` | `HomePage` | Landing page / Entry point |
| `/round/1` | `RoundPage` | Round 1 - Screening |
| `/round/2` | `RoundPage` | Round 2 - Technical |
| `/round/3` | `RoundPage` | Round 3 - Scenario |
| `/evaluation` | `EvaluationPage` | Final evaluation report |
| `*` (catch-all) | Redirect to `/` | Handles invalid routes |

---

## 🔀 Navigation Flow

### Linear Flow (Intended Path)
```
┌──────────────────────────────────────────────┐
│                                              │
│  Home Page (/)                               │
│  "Start Interview" Button                    │
│                                              │
└──────────────┬───────────────────────────────┘
               │ navigate('/round/1')
               ▼
┌──────────────────────────────────────────────┐
│                                              │
│  Round 1 - Screening (/round/1)              │
│  "Progress to Next Round" Button             │
│                                              │
└──────────────┬───────────────────────────────┘
               │ navigate('/round/2')
               ▼
┌──────────────────────────────────────────────┐
│                                              │
│  Round 2 - Technical (/round/2)              │
│  "Progress to Next Round" Button             │
│                                              │
└──────────────┬───────────────────────────────┘
               │ navigate('/round/3')
               ▼
┌──────────────────────────────────────────────┐
│                                              │
│  Round 3 - Scenario (/round/3)               │
│  "Complete Interview" Button                 │
│                                              │
└──────────────┬───────────────────────────────┘
               │ navigate('/evaluation')
               ▼
┌──────────────────────────────────────────────┐
│                                              │
│  Final Evaluation (/evaluation)              │
│  "Start New Interview" Button                │
│                                              │
└──────────────┬───────────────────────────────┘
               │ navigate('/')
               │
               └──────> Back to Home Page
```

---

## 🛠 Implementation Details

### App.jsx - Router Configuration
```jsx
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/round/:roundId" element={<RoundPage />} />
        <Route path="/evaluation" element={<EvaluationPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}
```

### Dynamic Route Parameters
The `/round/:roundId` route uses a dynamic parameter to handle all three rounds:
- `/round/1` → Round 1 (Screening)
- `/round/2` → Round 2 (Technical)
- `/round/3` → Round 3 (Scenario)

**RoundPage.jsx** extracts the round ID:
```jsx
const { roundId } = useParams();
const currentRound = parseInt(roundId);
```

---

## 🔄 Navigation Methods

### 1. Programmatic Navigation
Using the `useNavigate` hook:

```jsx
import { useNavigate } from 'react-router-dom';

const navigate = useNavigate();

// Navigate to next round
navigate('/round/2');

// Navigate to evaluation
navigate('/evaluation');

// Navigate back to home
navigate('/');
```

### 2. Link Components
For declarative navigation (not currently used, but available):

```jsx
import { Link } from 'react-router-dom';

<Link to="/round/1">Start Interview</Link>
<Link to="/evaluation">View Results</Link>
```

---

## 🛡️ Route Protection & Validation

### Invalid Round Handling
**RoundPage.jsx** validates the round ID:

```jsx
useEffect(() => {
  if (currentRound < 1 || currentRound > 3) {
    navigate('/');
  }
}, [currentRound, navigate]);
```

If a user tries to access `/round/5` or `/round/0`, they're redirected to home.

### Catch-All Route
Any unmatched routes redirect to the home page:

```jsx
<Route path="*" element={<Navigate to="/" replace />} />
```

Examples:
- `/round/invalid` → Redirects to `/`
- `/random-page` → Redirects to `/`
- `/round` → Redirects to `/`

---

## 📦 State Management Across Routes

### Challenge
Each route change creates a new component instance, losing local state.

### Current Approach
Each `RoundPage` instance initializes its own state:
- Messages start fresh for each round
- Round-specific welcome messages
- Independent conversation history

### Future Enhancement Options

#### Option 1: Context API
```jsx
// Create InterviewContext
const InterviewContext = createContext();

// Wrap app with provider
<InterviewProvider>
  <Router>...</Router>
</InterviewProvider>

// Access state in any component
const { messages, addMessage } = useContext(InterviewContext);
```

#### Option 2: Local Storage
```jsx
// Save state on route change
useEffect(() => {
  localStorage.setItem('interviewState', JSON.stringify(state));
}, [state]);

// Restore state on mount
useEffect(() => {
  const saved = localStorage.getItem('interviewState');
  if (saved) setState(JSON.parse(saved));
}, []);
```

#### Option 3: URL State (Query Parameters)
```jsx
// Pass state via URL
navigate('/round/2?msgCount=5&timestamp=123456');

// Read from URL
const [searchParams] = useSearchParams();
const msgCount = searchParams.get('msgCount');
```

---

## 🎯 Navigation Patterns

### Pattern 1: Sequential Progression
Used for moving through interview rounds:

```jsx
const handleNextRound = () => {
  if (currentRound < 3) {
    navigate(`/round/${currentRound + 1}`);
  } else {
    navigate('/evaluation');
  }
};
```

### Pattern 2: Restart Flow
Used to return to the beginning:

```jsx
const handleRestart = () => {
  navigate('/');
};
```

### Pattern 3: Direct Access
Users can manually type URLs:
- `/round/2` - Jump to technical round
- `/evaluation` - View evaluation (if accessible)

**Note**: No authentication/authorization currently prevents direct access.

---

## 🚀 Navigation Best Practices

### ✅ Do's
1. **Use `navigate()` for programmatic navigation**
   ```jsx
   navigate('/round/1');
   ```

2. **Validate route parameters**
   ```jsx
   if (currentRound < 1 || currentRound > 3) redirect();
   ```

3. **Use `replace` for redirects**
   ```jsx
   <Navigate to="/" replace />
   ```
   This prevents back button from going to invalid routes.

4. **Clean up on unmount**
   ```jsx
   useEffect(() => {
     return () => {
       // Cleanup code
     };
   }, []);
   ```

### ❌ Don'ts
1. **Don't use `<a>` tags for internal links**
   - Causes full page reload
   - Loses React state

2. **Don't forget error boundaries**
   - Handle navigation errors gracefully

3. **Don't hardcode routes everywhere**
   - Use constants or route configuration

---

## 🔧 Adding New Routes

### Step 1: Create Page Component
```jsx
// src/pages/NewPage.jsx
const NewPage = () => {
  return <div>New Page Content</div>;
};

export default NewPage;
```

### Step 2: Add Route to App.jsx
```jsx
import NewPage from './pages/NewPage';

<Routes>
  {/* Existing routes */}
  <Route path="/new-page" element={<NewPage />} />
</Routes>
```

### Step 3: Navigate to New Route
```jsx
navigate('/new-page');
```

---

## 🐛 Troubleshooting

### Issue: "404 on page refresh"
**Cause**: Server doesn't understand client-side routes

**Solution**: Configure dev server in `vite.config.js`:
```js
export default {
  server: {
    historyApiFallback: true
  }
}
```
or use HashRouter instead of BrowserRouter (not recommended).

### Issue: "State lost on navigation"
**Cause**: Each route creates new component instance

**Solutions**:
- Lift state to parent component
- Use Context API
- Use state management library (Redux, Zustand)
- Store in localStorage

### Issue: "Back button doesn't work as expected"
**Cause**: Using `replace: true` too often

**Solution**: Only use `replace` for redirects, not normal navigation.

---

## 📊 Route Analytics (Future Enhancement)

Track route changes for analytics:

```jsx
useEffect(() => {
  // Track page view
  analytics.track('Page View', {
    path: location.pathname,
    round: currentRound
  });
}, [location]);
```

---

## 🔐 Route Protection (Future Enhancement)

Add authentication/authorization:

```jsx
const ProtectedRoute = ({ children }) => {
  const { isAuthenticated } = useAuth();
  return isAuthenticated ? children : <Navigate to="/login" />;
};

<Route path="/round/:id" element={
  <ProtectedRoute>
    <RoundPage />
  </ProtectedRoute>
} />
```

---

## 📚 Related Documentation
- [React Router Documentation](https://reactrouter.com/)
- [src/App.jsx](../src/App.jsx) - Main routing configuration
- [src/pages/](../src/pages/) - All page components

---

**Last Updated**: February 2026
