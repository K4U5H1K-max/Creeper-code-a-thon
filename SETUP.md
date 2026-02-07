# Quick Setup Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
npm install
```

This will install:
- React 18.2.0
- React Router DOM 6.21.0
- Tailwind CSS 3.3.6
- Vite 5.0.8
- Lucide React (for icons)

**Estimated time**: 2-3 minutes

---

### Step 2: Start Development Server
```bash
npm run dev
```

The app will automatically open in your browser at `http://localhost:3000`

**What you'll see**:
- ✅ **Home Page** with "Start Interview" button
- ✅ Professional landing page layout
- ✅ Interview structure overview
- ✅ Clean, minimal design

---

### Step 3: Explore the Multi-Page Flow

#### Try These Actions:

1. **Start the Interview**
   - Click the "Start Interview" button
   - Navigate to Round 1 - Screening

2. **Send Messages**
   - Type in the input box at the bottom
   - Click "Send" or press Enter
   - Watch the AI typing indicator
   - See the response appear

3. **Progress Through Rounds**
   - Use the "Progress to Next Round" button in the demo controls
   - Navigate from Screening → Technical → Scenario
   - Watch the progress stepper update
   - Notice the URL changes for each round

4. **View Final Evaluation**
   - Complete all 3 rounds
   - Click "Complete Interview"
   - See the comprehensive evaluation report

5. **Restart Interview**
   - Click "Start New Interview" from evaluation page
   - Returns to home page

---

## 🧭 Page Navigation

### Application Flow
```
Home (/)
    ↓ Click "Start Interview"
Round 1: Screening (/round/1)
    ↓ Progress to Next Round
Round 2: Technical (/round/2)
    ↓ Progress to Next Round
Round 3: Scenario (/round/3)
    ↓ Complete Interview
Final Evaluation (/evaluation)
    ↓ Start New Interview
Home (/)
```

---

## 🔧 Customization Quick Tips

### Change Interview Rounds
**File**: [src/pages/RoundPage.jsx](src/pages/RoundPage.jsx) (lines 17-42)
```javascript
const rounds = [
  { 
    id: 1, 
    name: 'Screening', 
    description: 'Your description',
    focus: 'Focus area',
    welcomeMessage: 'AI greeting'
  },
  // ... more rounds
];
```

### Add New Route
**File**: [src/App.jsx](src/App.jsx)
```javascript
<Route path="/your-route" element={<YourPage />} />
```pages/RoundPage.jsx](src/pages/RoundPage.jsx) (lines 100-13

### Change Primary Color
**File**: [tailwind.config.js](tailwind.config.js)
```javascript
primary: {
  600: '#3b82f6', // Change this hex code
}
```

### Modify AI Responses
**File**: [src/App.jsx](src/App.jsx) (lines 64-80)
```javascript
const getAIResponse = (round, messageCount) => {
  // Add your custom responses here
}
```

---

## 📦 Build for Production

```bash
npm run build
```

Output will be in the `dist/` folder, ready to deploy to:
- Vercel
- Netlify
- GitHub Pages
- Any static hosting service

---

## 🐛 Troubleshooting

### Issue: npm install fails
**Solution**: Make sure you have Node.js 16+ installed
```bash
node --version  # Should be v16 or higher
```

### Issue: Port 3000 already in use
**Solution**: The app will use the next available port automatically, or you can change it in [vite.config.js](vite.config.js)

### Issue: Styles not applied
**Solution**: Make sure Tailwind CSS is properly installed
```bash
npm install -D tailwindcss postcss autoprefixer
```

### Issue: Icons not showing
**Solution**: Reinstall lucide-react
```bash
npm install lucide-react
```

---

## 💡 Pro Tips for Demo

1. **Start Fresh**: Begin demo on the home page to show the complete flow
2. **Prepare Sample Answers**: Have 2-3 pre-written responses ready to showcase quickly
3. **Use Demo Controls**: Don't wait for natural conversation flow - use the progression buttons
4. **Show Navigation**: Highlight how URLs change as you progress through rounds
5. **Highlight Key Features**: 
   - Multi-page architecture
   - Clean page transitions
   - Progress persistence across pages
   - Professional landing page
   - Comprehensive evaluation
6. **Explain The Vision**: Talk about how this would connect to a real AI backend
7. **Emphasize Professionalism**: Point out the enterprise-grade UI design

---

## 📞 Need Help?

- Check [README.md](README.md) for full documentation
- Review [COMPONENTS.md](COMPONENTS.md) for component details
- Inspect component files - they're heavily commented!

---

**Ready to impress? Run `npm run dev` and showcase your AI Interview Platform! 🚀**
