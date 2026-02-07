# AI Interview Platform - Multi-Page Interview Flow

A modern, professional, and interactive multi-page interface for an AI-powered interview platform. Built with React, React Router, and Tailwind CSS.

![AI Interview Platform](https://img.shields.io/badge/React-18.2.0-blue)
![React Router](https://img.shields.io/badge/React_Router-6.21.0-red)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-3.3.6-38B2AC)
![Vite](https://img.shields.io/badge/Vite-5.0.8-646CFF)

## 🎯 Features

### Multi-Page Flow
The application follows a structured, linear interview flow across multiple pages:

1. **Home Page** (`/`) - Landing page with "Start Interview" button
2. **Round 1 - Screening** (`/round/1`) - Behavioral & HR discussion
3. **Round 2 - Technical** (`/round/2`) - Skills & knowledge assessment
4. **Round 3 - Scenario** (`/round/3`) - Problem-solving & case studies
5. **Final Evaluation** (`/evaluation`) - Comprehensive assessment report

### Professional Enterprise UI
- Clean, minimal design inspired by modern SaaS platforms (Google Hire, Lever)
- Neutral professional color palette (white, light gray, blue accents)
- Desktop-first responsive layout
- Smooth page transitions and professional typography

### Interview Management
- **Multi-page flow**: Separate pages for each interview stage
- **Routing**: React Router for smooth navigation
- **Three interview rounds**: 
  - Round 1: Screening (Behavioral & HR)
  - Round 2: Technical (Skills assessment)
  - Round 3: Scenario (Problem-solving)
- **Real-time chat interface**: Natural conversation between AI and candidate
- **Progress tracking**: Visual stepper showing current round across all pages
- **Context panel**: Round-specific information and interview tips
- **Final evaluation**: Comprehensive assessment report at the end

### UI Pages & Components
- ✅ **Home Page**: Welcome screen with interview overview and start button
- ✅ **Round Pages**: Shared layout for all three interview rounds
- ✅ **Header**: App branding and interview status indicator (persistent)
- ✅ **Progress Stepper**: Visual round progression tracker (persistent)
- ✅ **Interview Chat**: Chat-style conversation layout with typing indicators
- ✅ **Context Panel**: Current round info and guidelines
- ✅ **Final Evaluation Page**: Professional report-style results view

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ and npm/yarn installed

### Installation

1. **Clone or navigate to the repository**
   ```bash
   cd Creeper-code-a-thon
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:3000`
   - If not, manually navigate to the URL shown in terminal

### Build for Production

```bash
npm run build
```

The optipages/
│   │   ├── HomePage.jsx            # Landing page with start button
│   │   ├── RoundPage.jsx           # Shared round page (1, 2, 3)
│   │   └── EvaluationPage.jsx      # Final evaluation page
│   ├── components/
│   │   ├── Header.jsx              # App header with status
│   │   ├── ProgressStepper.jsx     # Round progress indicator
│   │   ├── InterviewChat.jsx       # Main chat interface
│   │   ├── ContextPanel.jsx        # Round information panel
│   │   └── FinalEvaluation.jsx     # Results/evaluation view
│   ├── App.jsx                     # Main app with routing
│   ├── components/
│   │   ├── Header.jsx              # App header with status
│   │   ├── ProgressStepper.jsx     # Round progress indicator
│   │   ├── InterviewChat.jsx       # Main chat interface
│   │   ├── ContextPanel.jsx        # Round information panel
│   │   └── FinalEvaluation.jsx     # Results/evaluation view
│   ├── App.jsx                     # Main application component
│   ├── main.jsx                    # Application entry point
│   └── index.css                   # Global styles
├── index.html
├── package.json
├── vite.config.js
├── tailwind.config.js
└── postcss.config.js
```

## 🎨 Design System

### Color Palette
- **Primary Blue**: Used for CTAs, active states, and branding
  - `#3b82f6` (primary-600)
  - `#2563eb` (primary-700)
  

### Page Flow
```
Home Page (/)
    ↓
Round 1: Screening (/round/1)
    ↓
Round 2: Technical (/round/2)
    ↓
Round 3: Scenario (/round/3)
    ↓
Final Evaluation (/evaluation)
```
- **Neutral Grays**: Background pages/RoundPage.jsx](src/pages/RoundPage.jsx):

```javascript
const rounds = [
  { 
    id: 1, 
    name: 'Screening', 
    description: 'Your description',
    focus: 'Focus area description',
    welcomeMessage: 'AI greeting message'
  },
  // ... more rounds
];
```

### Adding New Routes
Update [src/App.jsx](src/App.jsx):

```javascript
<Route path="/your-route" element={<YourComponent />} />**Sizes**: Responsive scale from 0.75rem to 2rem

### Spacing
- Consistent 4px/8px grid system
- Card padding: 1.5rem (24px)
- Section gaps: 1.5rem (24px)

## 🔧 Customization

### Changing Interview Rounds
Edit the `rounds` array in [src/App.jsx](src/App.jsx):

```javascript
const rounds = [
  { id: 1, name: 'Screening', description: 'Your description' },
  { id: 2, name: 'Technical', description: 'Your description' },
  { id: 3, name: 'Scenario', description: 'Your description' }
];
```

### Modifying Colors
Update [tailwind.config.js](tailwind.config.js) color definitions:

```javascript
colors: Router for navigation and routing
- React useState hooks for local component state
- Props drilling for parent-child communication
- URL parameters for round identif
    600: '#your-color',
    // ... other shades
  }
}
```

### Adding New Components
1. Create new component file in `src/components/`
2. Import and use in [src/App.jsx](src/App.jsx)
3. Follow existing component structure and naming conventions

## 🎭 Demo Features

The current implementation includes demo controls to simulate:
- Progressing between interview rounds
- Completing the interview
- Viewing final evaluation

These are for demonstration purposes and can be removed or modified for production use.

## 🏗️ Architecture

### State Management
- React useState hooks for local component state
- Props drilling for parent-child communication
- Can be easily upgraded to Context API or Redux if needed

### Component Design
- Functional components with hooks
- Props documentation in JSDoc comments
- Clear separation of concerns
- Reusable and modular structure
Flow
1. **Start at Home Page** - Show clean landing page
2. **Click "Start Interview"** - Navigate to Round 1
3. **Demonstrate chat** - Send sample messages
4. **Progress through rounds** - Use demo controls
5. **Show final evaluation** - Display comprehensive report
6. **Highlight navigation** - Show page transitions

### Key Talking Points
- Multi-page application architecture
- React Router implementation
Main layout uses CSS Grid that adapts:
- Mobile: Single column stack
- Desktop: 2/3 chat area + 1/3 context panel

## 🎓 For Hackathon Demo

### Presentation Tips
1. Start with the progress stepper to show round structure
2. Demonstrate the chat interface with sample interactions
3. Use demo controls to progress through rounds quickly
4. Show the final evaluation report
5. Highlight the professional, clean design

### Key Talking Points
- Enterprise-grade UI/UX design
- Realistic interview flow (not gamified)
- Comprehensive evaluation system
- Scalable component architecture
- Production-ready code quality

## 🔮 Future Enhancements

- [ ] Backend API integration for real AI responses
- [ ] User authentication and session management
- [ ] Interview recording and playback
- [ ] Analytics dashboard for recruiters
- [ ] Multi-language support
- [ ] Dark mode theme
- [ ] Export evaluation reports as PDF
- [ ] Real-time collaboration features

## 📄 License

This project is created for educational/hackathon purposes.

## 🤝 Contributing

This is a hackathon project. Feel free to fork and customize for your needs!

---

**Built with ❤️ for Creeper Code-a-thon 2026**
