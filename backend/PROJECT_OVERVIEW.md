# Multi-Round AI Interview System - Complete Project

A production-ready AI-powered interview platform that conducts multi-round technical interviews with intelligent evaluation and scoring.

## 🎯 Project Overview

This system simulates a real hiring process with three progressive interview rounds:
- **Round 1: Screening** - Filters basic qualifications (4 questions, 60% pass)
- **Round 2: Technical** - Deep technical assessment (5 questions, 65% pass)  
- **Round 3: Scenario** - Real-world problem solving (3 questions, 70% pass)

### Key Features

✅ **Intelligent Multi-Round Flow**
- Sequential rounds with pass/fail gates
- Different AI models for each round
- Progressive difficulty increase

✅ **Smart Evaluation System**
- Real-time response quality analysis
- AI feedback sentiment analysis
- Weighted scoring across rounds
- Final batch assignment (A+ to D)

✅ **Production Ready**
- RESTful API design
- Comprehensive error handling
- Session management
- CORS enabled for frontend integration

✅ **Developer Friendly**
- Well-documented code
- Pydantic models for type safety
- Modular architecture
- Easy to extend and customize

## 📁 Project Structure

```
Creeper final/
├── frontend/                    # React frontend (already built)
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   └── context/
│   └── package.json
│
└── backend/                     # Python Flask backend (NEW)
    ├── app.py                   # Main Flask application
    ├── models.py                # Pydantic data models
    ├── groq_service.py          # Groq API integration
    ├── evaluator.py             # Evaluation & scoring logic
    ├── prompts.py               # System prompts for each round
    ├── requirements.txt         # Python dependencies
    ├── .env.example             # Environment template
    ├── README.md                # Complete API documentation
    ├── SETUP.md                 # Quick setup guide
    ├── FRONTEND_INTEGRATION.md  # Frontend integration guide
    └── test_api.py              # API testing script
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Groq API key ([Get it here](https://console.groq.com/keys))

### Backend Setup (3 steps)

```bash
# 1. Install dependencies
cd backend
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt

# 2. Configure API key
copy .env.example .env      # Windows
# Edit .env and add your GROQ_API_KEY

# 3. Run server
python app.py
# Server starts on http://localhost:5000
```

### Frontend Setup

```bash
# Install and run
npm install
npm run dev
# Frontend starts on http://localhost:5173
```

### Test Backend

```bash
# Terminal 1: Run backend
cd backend
python app.py

# Terminal 2: Run tests
python test_api.py
```

## 🏗️ Architecture

### Backend Components

1. **app.py** - Flask application with 5 endpoints:
   - `GET /health` - Health check
   - `POST /api/start-interview` - Initialize interview
   - `POST /api/chat` - Send/receive messages
   - `GET /api/session/{id}` - Get session status
   - `GET /api/session/{id}/history` - Get conversation history

2. **models.py** - Type-safe data models:
   - `InterviewSession` - Complete interview state
   - `RoundData` - Round-specific data
   - `Message` - Conversation messages
   - `QuestionAnswer` - Q&A pairs with scores

3. **groq_service.py** - AI integration:
   - Different models per round
   - Greeting generation
   - Dynamic question asking
   - Answer evaluation

4. **evaluator.py** - Intelligent scoring:
   - Response quality analysis
   - AI feedback sentiment analysis
   - Round score calculation
   - Final evaluation with batch assignment

5. **prompts.py** - Carefully crafted system prompts:
   - Round-specific instructions
   - Question count enforcement
   - Evaluation criteria
   - Red flag detection

### Interview Flow

```
User Selects Job Role
         ↓
   Start Interview
         ↓
┌─────────────────────┐
│  Round 1: Screening │ (4 questions)
│  Pass: ≥60%         │
└──────────┬──────────┘
           │
    [Pass] ├─→ Continue
           │   [Fail] → Interview Ends
           ↓
┌─────────────────────┐
│  Round 2: Technical │ (5 questions)
│  Pass: ≥65%         │
└──────────┬──────────┘
           │
    [Pass] ├─→ Continue
           │   [Fail] → Interview Ends
           ↓
┌─────────────────────┐
│  Round 3: Scenario  │ (3 questions)
│  Pass: ≥70%         │
└──────────┬──────────┘
           │
    [Pass] │
           ↓
  Final Evaluation
  • Overall Score
  • Confidence Score
  • Batch (A+ to D)
  • Recommendation
```

## 🎯 Evaluation System

### Scoring Methodology

**Per Question:**
- Length analysis (10-300 words optimal)
- Coherence check (sentence structure)
- Relevance detection (technical terms)
- AI feedback sentiment (70% weight)

**Per Round:**
- Weighted average of question scores
- Technical round: later questions weighted higher
- Pass/fail based on threshold

**Final Evaluation:**
- Round 1: 20% weight (Screening)
- Round 2: 45% weight (Technical)
- Round 3: 35% weight (Scenario)

### Batch Assignment

| Batch | Score Range | Description |
|-------|-------------|-------------|
| A+ | 90-100% | Exceptional candidate |
| A | 80-89% | Strong hire |
| B+ | 70-79% | Good candidate |
| B | 60-69% | Consider for junior roles |
| C | 50-59% | Needs development |
| D | 0-49% | Not recommended |

## 🔌 API Reference

### Start Interview
```http
POST /api/start-interview
Content-Type: application/json

{
  "job_role": "Software Engineer",
  "candidate_name": "John Doe"
}
```

**Response:**
```json
{
  "session_id": "uuid",
  "job_role": "Software Engineer",
  "current_round": 1,
  "round_name": "Screening Round",
  "greeting": "Welcome! Let me explain...",
  "total_questions": 4
}
```

### Send Message
```http
POST /api/chat
Content-Type: application/json

{
  "session_id": "uuid",
  "message": "I have 5 years of experience..."
}
```

**Response:**
```json
{
  "session_id": "uuid",
  "ai_message": "Great! Let me ask you...",
  "current_round": 1,
  "current_question": 2,
  "total_questions": 4,
  "round_complete": false
}
```

**Full API docs:** See [backend/README.md](backend/README.md)

## 🧪 Testing

### Manual Testing
```bash
# Test health
curl http://localhost:5000/health

# Start interview
curl -X POST http://localhost:5000/api/start-interview \
  -H "Content-Type: application/json" \
  -d '{"job_role": "Software Engineer"}'
```

### Automated Testing
```bash
cd backend
python test_api.py
```

The test script will:
- ✅ Check health endpoint
- ✅ Start a new interview
- ✅ Answer all 4 screening questions
- ✅ Verify round completion
- ✅ Check session retrieval
- ✅ Verify conversation history

## 🎨 Frontend Integration

The backend is designed to work seamlessly with your existing React frontend.

**Integration Steps:**
1. Create API service (`src/services/api.js`)
2. Set up Interview Context (`src/context/InterviewContext.jsx`)
3. Update components to use the context
4. Connect InterviewChat and ProgressStepper

**Complete guide:** See [backend/FRONTEND_INTEGRATION.md](backend/FRONTEND_INTEGRATION.md)

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [README.md](backend/README.md) | Complete API documentation & architecture |
| [SETUP.md](backend/SETUP.md) | Quick setup guide (3 steps) |
| [FRONTEND_INTEGRATION.md](backend/FRONTEND_INTEGRATION.md) | React frontend integration |
| This file | Project overview |

## 🔒 Environment Variables

```env
GROQ_API_KEY=your_groq_api_key_here    # Required
PORT=5000                               # Optional (default: 5000)
FLASK_ENV=development                   # Optional (default: development)
```

## 🚢 Deployment

### Backend
**Options:** Heroku, Railway, Render, AWS

```bash
# Add gunicorn to requirements.txt
gunicorn==21.2.0

# Create Procfile
web: gunicorn app:app

# Set environment variables
GROQ_API_KEY=your_key
```

### Frontend
**Options:** Vercel, Netlify

```bash
# Update API URL
VITE_API_BASE_URL=https://your-backend.com/api

# Build
npm run build
```

## 🛠️ Customization

### Add New Round
1. Update `prompts.py` - Add system prompt
2. Update `ROUND_THRESHOLDS` in `evaluator.py`
3. Update frontend round configuration

### Change Question Count
1. Modify `get_round_info()` in `prompts.py`
2. Update system prompts to reflect new count

### Adjust Scoring
1. Modify weights in `evaluator.py`
2. Adjust thresholds per round
3. Customize batch criteria

### Use Different AI Models
1. Update `ROUND_MODELS` in `groq_service.py`
2. Available models (as of Feb 2026):
   - `llama-3.3-70b-versatile` (currently used for all rounds)
   - `gemma2-9b-it` (lighter, faster alternative)
   - `llama3-groq-70b-8192-tool-use-preview` (for tool use)
   - Check https://console.groq.com/docs/models for latest

## 🐛 Troubleshooting

### "GROQ_API_KEY not found"
- Ensure `.env` file exists in `backend/` directory
- Check API key is valid at [console.groq.com](https://console.groq.com)

### "Port already in use"
- Change `PORT` in `.env`
- Or kill the process using port 5000

### "Session not found"
- Sessions are stored in-memory (reset on server restart)
- Use session_id from `/api/start-interview` response
- Implement Redis for production persistence

### CORS issues
- Backend has CORS enabled by default
- For production, configure specific origins in `app.py`

## 📊 System Prompts Preview

Each round has a foolproof system prompt that:
- **Enforces exact question count** (4, 5, 3)
- **Defines evaluation criteria** clearly
- **Provides question progression** guidelines
- **Identifies red flags** to watch for
- **Sets the right tone** for each round type

**Example (Round 1 - Screening):**
```
You are an expert HR screening interviewer...

CRITICAL INSTRUCTIONS:
1. You MUST ask EXACTLY 4 questions - no more, no less
2. Ask ONE question at a time and wait for response
3. Keep track of question number (1/4, 2/4, 3/4, 4/4)
...
```

Full prompts are in [backend/prompts.py](backend/prompts.py)

## 💡 Key Features

### 1. Intelligent Question Flow
- AI asks contextual follow-up questions
- Progressive difficulty in technical round
- Natural conversation flow (no "Question 1/4" labels)

### 2. Real-time Evaluation
- Each answer scored immediately
- AI feedback analyzed for sentiment
- Running score tracked per round

### 3. Multi-Model Architecture
- Different AI models per round
- Optimized for specific interview types
- Ensures variety and appropriate expertise

### 4. Comprehensive Scoring
- 7+ evaluation criteria per response
- Weighted scoring across rounds
- Confidence score based on consistency

### 5. Production Ready
- Type-safe with Pydantic models
- Error handling at every level
- Session management
- API versioning ready
- Logging support

## 🎓 Learning Resources

**Groq API:**
- [Groq Documentation](https://console.groq.com/docs)
- [Available Models](https://console.groq.com/docs/models)

**Flask:**
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)

**Pydantic:**
- [Pydantic Documentation](https://docs.pydantic.dev/)

## 📝 License

MIT License - Feel free to use and modify for your needs.

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Add database persistence (PostgreSQL/MongoDB)
- Implement Redis for session storage
- Add audio/video interview support
- Create admin dashboard
- Add analytics and insights
- Support for multiple languages

## ✨ Credits

Built with:
- **Flask** - Web framework
- **Groq** - AI API
- **Pydantic** - Data validation
- **React** - Frontend framework
- **TailwindCSS** - Styling

---

**Ready to get started?** Follow the [Quick Start](#-quick-start) guide above!

For questions or issues, check the documentation files or create an issue.

Happy interviewing! 🚀
